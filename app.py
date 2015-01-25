from flask import Flask, session, redirect, url_for, escape, request, render_template, flash
from functools import wraps
import base

app = Flask(__name__)

#NOT NEEDED? BASE ALREADY HAS A VALIDATE
#def validate(func):
#    @wraps(func)
#    def inner (*args, **kwargs):
#        error = None
#        if request.method == 'POST':
#            if base.validate (request.form['username'], request.form['password']):
#               session['username'] = request.form['username']
#                flash('You were successfully logged in')
#               return redirect(url_for('index'))
#            else:
#                error = "Invalid credentials"
#                return render_template ("login.html", error = error)
#        return func()
#    return inner

@app.route('/')
def index():
    username = "NOT LOGGED IN"
    if 'username' in session:
        username = "LOGGED IN AS " + escape(session['username'])
    return render_template ("index.html", username = username)


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    flash("You have logged out")
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        flash("You're already logged in as " + escape(session['username']))
        return redirect(url_for("index"));
    try:
        if request.form["login"] != None:
            if base.validate(request.form['username'], request.form['password']):
                print("yolo")
                session['username'] = request.form['username']
                flash('You were successfully logged in')
                print("YOU LOGGED IN CONTRASGOITR")
                return redirect(url_for('index'))
            else:
                flash("invalid credentials")
                #error = "Invalid credentials"
                return render_template ("login.html"
                                        #, error = error
                )
    except:
        print("YOURE OUT OF THE LOGIN")
    try:
        if request.form["register"] != None:
            print("YOURE IN REGISTER")
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
        print("YOURE OUT OF REGISTER")
    return render_template("login.html")

#HAVE INPUTS FOR 'username' 'password' AND 'newpassword'
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    '''
    #error = None
    if 'username' in session:
        if request.form['newpw1'] != request.form['newpw2']:
            flash("your passwords don't match")
        if base.updateUser(escape(session['username']), request.form['oldpw'], request.form['newpw1']):
               flash("Info updated")
        else:
               flash("wrong password")
    else:
        flash("You are not logged in")
        return redirect(url_for(index))
    '''
    return render_template("settings.html")
    
@app.route('/reset')
def reset():
    base.restart()
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
#this is fake very fake oooh
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.debug = True
    app.run(host = "127.0.0.1", port = 1247)
