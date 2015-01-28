from flask import Flask, session, redirect, url_for, escape, request, render_template, flash
from functools import wraps
import base

app = Flask(__name__)

@app.route('/')
def index():
    #base.printUsers()
    print base.gameONcheck()
            
    if 'username' in session:
        return render_template ("index.html", 
                                corner = session['username'])
    return render_template ("index.html")

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
        flash("You have logged out")
    else:
        flash("You are not logged in")
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        flash("You're already logged in as " + escape(session['username']))
        return redirect(url_for("index"));
    try:
        if request.form["login"] != None:
            print(request.form['username'])
            if base.validate(request.form['username'], request.form['password']):
                session['username'] = request.form['username']
                flash('You were successfully logged in')
                return redirect(url_for('index'))
            else:
                flash("invalid credentials")
                return render_template ("login.html")
    except:
        pass
    try:
        if request.form["register"] != None:
            if (request.form["password1"] != request.form["password2"]):
                flash("Passwords don't match")
                return redirect(url_for("login"))
            if base.addUser(request.form['username'], request.form['password1']):
                session['username'] = request.form['username']
                flash ("You have successfully registered")
                return redirect(url_for('index'))
            else:
                flash("That username is already taken")
                return  render_template ("login.html")
    except:
        pass
    return render_template("login.html")

#HAVE INPUTS FOR 'username' 'password' AND 'newpassword'
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    base.printUsers()
    if 'username' in session:
        try:
            if request.form['submit'] != None:
                if request.form['newpw1'] != request.form['newpw2']:
                    flash("Your passwords don't match")
                elif base.updateUser(escape(session['username']), request.form['oldpw'], request.form['newpw1']):
                    flash("Info updated")
                else:
                    flash("Incorrect password")
        except:
            pass
    else:
        flash("You are not logged in")
        return redirect(url_for("index"))
    return render_template("settings.html", 
                           corner = session['username'])
                    


@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'username' in session:
        if base.gameONcheck():
            print "BEFORE UPDATE"
            base.printData()
            uid = base.getID(session['username'])
            tid = base.getTargetID(uid)
            return render_template ("game.html",
                                    corner = session['username'],
                                    username = session['username'], 
                                    target = base.getName(tid)
            )
        else:
            flash("Anathema has yet to begin")
            return redirect(url_for("index"))
    else:
        flash("You are not logged in")
        return redirect(url_for("index"))

##updates locations
@app.route('/status', methods=['GET', 'POST'])
def status ():
    if 'username' in session:
        if base.gameONcheck():
            print "AFTER UPDATE"
            base.printData()
            uid = base.getID(session['username'])
            tid = base.getTargetID(uid)
            print tid
            u = base.checkStatus(uid)
            t = base.checkStatus(tid)
            us = ""
            ts = ""
            if (u):
                us = "Alive"
            else:
                #flash ("Sorry, you have been killed")
                #return redirect (url_for("index"))
                us = "Dead"
            
            if (t):
                ts = "Alive"
            else:
                #flash ("Sorry, you have been killed")
                #return redirect (url_for("index"))
                ts = "Dead"
            #print u
            #print t
            return render_template ("status.html", 
                            corner = session['username'],
                            user_status = us,
                            target_status = ts)
        else: 
            flash("Anathema has yet to begin")
            return redirect(url_for("index"))
    else:
        flash("You are not logged in")
        return redirect(url_for("index"))
            

#killed, reassign
@app.route('/kill', methods=['GET', 'POST'])
def kill():
    if 'username' in session:
        if base.gameONcheck():
            uid = base.getID(session['username'])
            tid = base.getTargetID(uid)
            lat1 = base.getLat(uid)
            long1 = base.getLong(uid)
            lat2 = base.getLat(tid)
            long2 = base.getLong(tid)
            #print lat1
            #print long1
            #print lat2
            #print long2
            if (base.killCheck (lat1, long1, lat2, long2)):
                base.kill(tid)
                if ( base.checkWin(uid)):
                    flash ("You have won! Congrats!")
                    return redirect (url_for ("switch"))

                else:
                    base.assignTargets()
                    flash ("You have killed your target! You have been assigned another target.")
                    return redirect (url_for ("game"))

            else: 
                flash ("You have failed to kill your target.")
                return redirect (url_for ("game"))
        else: 
            flash("Anathema has yet to begin")
            return redirect(url_for("index"))
    else:
        flash("You are not logged in")
        return redirect(url_for("index"))
    

@app.route('/map', methods=['GET', 'POST'])
def map():
    uid = base.getID(session['username'])
    tid = base.getTargetID(uid)
    return render_template ("map.html", 
                            corner = session['username'],
                            ulat = base.getLat (uid),
                            ulong = base.getLong (uid),
                            tlat = base.getLat (tid),
                            tlong = base.getLong (tid)
                        )

@app.route('/target', methods=['GET', 'POST'])
def target():
    if 'username' in session:
        print "AFTER LOAD GAME"
        uid = base.getID(session['username'])      
        mylat = request.args.get('mylat')
        mylong = request.args.get('mylng') ##replace and run
        base.updateLat (uid, mylat) #will upload into mongo
        base.updateLong (uid, mylong)
        base.printData()
    return "hi"

@app.route('/restart', methods=['GET', 'POST'])
def restart():
    base.restart()
    base.assignTargets()
    return redirect (url_for ("index"))

@app.route('/switch', methods=['GET', 'POST'])
def switch():
    base.gameON()
    if (base.gameONcheck()):
        print base.gameONcheck()
        base.assignTargets()
    else:
        print base.gameONcheck()
        base.reset()
    return redirect(url_for("index"))

    
# set the secret key.  keep this really secret:
#this is fake very fake oooh
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.debug = True
    app.run(host = "127.0.0.1", port = 1247)
