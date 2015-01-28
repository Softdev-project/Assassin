from flask import Flask, session, redirect, url_for, escape, request, render_template, flash
from functools import wraps
import base

app = Flask(__name__)

@app.route('/')
def index():
    base.printUsers()
    if 'username' in session:
        return render_template ("index.html", 
                                corner = session['username'])
    return render_template ("index.html")

@app.route('/logout')
def logout():
    #base.printUsers()
    # remove the username from the session if it's there
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
                #error = "Invalid credentials"
                return render_template ("login.html"
                                        #, error = error
                )
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
                return  render_template ("register.html"
                                         #,error = error
                                     )
    except:
        pass
    return render_template("login.html")

#HAVE INPUTS FOR 'username' 'password' AND 'newpassword'
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    base.printUsers()
    #error = None

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
            return render_template ("game.html",
                                    corner = session['username'],
                                    #username
                                    #target
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
    uid = base.getID(session['username'])
    tid = base.getTargetID(uid)
    print tid
    u = base.checkStatus(uid)
    t = base.checkStatus(tid)
    print u
    print t
    return "hi"
"""
    return render_template ("status.html", 
                            corner = session['username'],
                            #user_status = get,
                            #target_status = get
                        )"""
#killed, reassign
@app.route('/kill', methods=['GET', 'POST'])
def kill():
    return render_template ("kill.html", corner = session['username'])

@app.route('/map', methods=['GET', 'POST'])
def map():
    return render_template ("map.html", 
                            corner = session['username']
                            #ulat
                            #ulong
                            #tlat
                            #tlong
                        )

@app.route('/restart', methods=['GET', 'POST'])
def restart():
    base.restart()

@app.route('/switch', methods=['GET', 'POST'])
def switch():
    if (base.gameON()):
        base.assignTargets()
    else:
        base.restart()
    return redirect(url_for("index"))

    
# set the secret key.  keep this really secret:
#this is fake very fake oooh
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.debug = True
    app.run(host = "127.0.0.1", port = 1247)
