from flask import Flask, render_template
from flask_auth import HTTPBasicAuth
import pdb

#pdb.set_trace()

app = Flask(__name__)
#pdb.set_trace()
auth = HTTPBasicAuth()
#pdb.set_trace()
users = [
    {'username': 'Tom', 'password': '111111'},
    {'username': 'brian', 'password': '123456'}
]
 
@auth.get_password
def get_password(username):
    for user in users:
        if user['username'] == username:
            return user['password']
    return None
#pdb.set_trace()
@app.route('/')
@auth.login_required
def index():
    app.logger.info('%s logged in successfully', auth.username())
    #return "Hello, %s!" % auth.username()
    return render_template('hello.html', username=auth.username())