# coding=utf-8
import flask
from flask import render_template, redirect, url_for, Response, send_file
from flask import request
from flask_httpauth import HTTPBasicAuth

app = flask.Flask(__name__)
auth = HTTPBasicAuth()

users = [
    {'username': 'admin', 'password': '123456'},
    {'username': 'Michael', 'password': '123456'}
]


@auth.get_password
def get_password(username):
    for user in users:
        if user['username'] == username:
            return user['password']
    return None


@app.route('/home/')
def home():
    return render_template('home.html', username=request.args.get('username'))


@app.route('/', methods=['POST', 'GET'])
@auth.login_required
def login():
    print('++++++++++++++++++++++++++', request.args.get("username"), request)
    return redirect(url_for('home', username=auth.username()))

if __name__ == '__main__':
    app.debug = True
    app.run('10.11.58.219', 80)
