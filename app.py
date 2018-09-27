import os
import requests
import redis
import json
import asyncio
from functools import wraps
from math import floor
import re
from requests_oauthlib import OAuth2Session
from flask import Flask, session, request, url_for, render_template, redirect, \
 jsonify, flash, abort, Response, send_file
from itsdangerous import JSONWebSignatureSerializer
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY",
                                          "dawdawdadwa&çed&ndlnad&pjéà&jdndqld"
                                          )
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload')
def upload_file():
   return render_template('uploader.html')

@app.route('/uploader', methods = ['GET','POST'])
def file():
   if request.method == 'POST':
       file = request.files['file']
       if file:
           file.save(os.path.join("images/", file.filename))
           return redirect("/i/{}".format(file.filename)), 308
       else:
           return "No File Supplied", 400

@app.route('/sharex', methods = ['GET','POST'])
def sharex():
   if request.method == 'POST':
       file = request.files['file']
       if file:
           file.save(os.path.join("images/", file.filename))
           return "https://you-dont-see.me/i/{}".format(file.filename), 200
       else:
           return "No File Supplied", 400

@app.route('/i/<string:name>', methods = ['GET'])
def get_file(name):
      return send_file(os.path.join("images/", name))

@app.route('/no-one-can-you')
def home():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
   app.run(debug = False, threaded=True)
