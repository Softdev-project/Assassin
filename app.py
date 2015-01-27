from flask import Flask, session, redirect, url_for, escape, request, render_template, flash
from functools import wraps
import base

app = Flask(__name__)

@app.route('/')
def index():
    base.printUsers()
    username = "NOT LOGGED IN"
    if 'username' in session:
        username = "LOGGED IN AS " + escape(session['username'])
        return render_template ("index.html", 
                                username = username,
                                corner = session['username'])
    return render_template ("index.html", 
                            username = username,)


@app.route('/logout')
def logout():
    base.printUsers()
    # remove the username from the session if it's there
    if 'username' in session:
        session.pop('username', None)
        flash("You have logged out")
    else:
        flash("You are not logged in")
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    base.printUsers()
    if 'username' in session:
        flash("You're already logged in as " + escape(session['username']))
        return redirect(url_for("index"));
    try:
        if request.form["login"] != None:
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
                print("HALLELUJAH")
                if request.form['newpw1'] != request.form['newpw2']:
                    flash("your passwords don't match")
                elif base.updateUser(escape(session['username']), request.form['oldpw'], request.form['newpw1']):
                    flash("Info updated")
                else:
                    flash("wrong password")
        except:
            pass
    else:
        flash("You are not logged in")
        return redirect(url_for("index"))
    return render_template("settings.html", 
                           corner = session['username'])
    
@app.route('/setup', methods=['GET', 'POST'])



@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'username' in session:
        if base.gameONcheck():
            return render_template ("game.html",
                                    corner = session['username'])
        else:
            flash("Anathema has yet to begin")
            return redirect(url_for("index"))
    else:
        flash("You are not logged in")
        return redirect(url_for("index"))

@app.route('/status', methods=['GET', 'POST'])
def status ():
    return render_template ("status.html", corner = session['username'])

@app.route('/kill', methods=['GET', 'POST'])
def kill():
    return render_template ("kill.html", corner = session['username'])

@app.route('/map', methods=['GET', 'POST'])
def map():
    return render_template ("map.html", corner = session['username'])

@app.route('/restart', methods=['GET', 'POST'])
def restart():
    base.restart()

@app.route('/switch', methods=['GET', 'POST'])
def switch():
    base.gameON()
    base.assignTargets()
    return redirect(url_for("index"))

    
# set the secret key.  keep this really secret:
#this is fake very fake oooh
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.debug = True
    app.run(host = "127.0.0.1", port = 1247)
