#!/usr/bin/python

from flask import Flask, render_template, abort, redirect, url_for, escape, request, session

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    if 'username' in session:
        if session['username'] !='':
            print "session name is %s" % session['username']
            return "Logged in as %s <br/><a href='/logout'>Logout</a>" % escape(session['username'])
        else:
            return "You did not input a username. <br/><a href='/logout'>Logout</a>"
    return '''You are not logged in. <br/><a href='/login'>Login</a>
    '''

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/red')
def red():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))



# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run()
