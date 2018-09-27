import os
import requests
import json
import re
from flask import Flask, session, request, url_for, render_template, redirect, \
 jsonify, flash, abort, Response, send_file
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

if __name__ == '__main__':
   app.run(debug = False, threaded=True)
