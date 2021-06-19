# -*- coding: utf-8 -*-
"""
Created on Sun July 26 2020

@author: Dhruv Singh
"""

from flask import Flask, render_template, request, session, redirect, url_for, flash
import os    

UPLOAD_FOLDER = './flask app/assets/images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
# Create Database if it doesnt exist

app = Flask(__name__,static_url_path='/assets',
            static_folder='./flask app/assets',
            template_folder='./flask app')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def root():
   return render_template('index.html')

@app.route('/index.html')
def index():
   return render_template('index.html')

@app.route('/contact.html')
def contact():
   return render_template('contact.html')

@app.route('/news.html')
def news():
   return render_template('news.html')

@app.route('/about.html')
def about():
   return render_template('about.html')

@app.route('/faqs.html')
def faqs():
   return render_template('faqs.html')

@app.route('/schemes.html')
def schemes():
   return render_template('schemes.html')


@app.route('/aschemes.html')
def aschemes():
   return render_template('aschemes.html')

# @app.route('/adminhome.html')
# @app.route('/adminhome.html', methods=['GET', 'POST'])
@app.route("/adminhome.html", methods=["GET", "POST"])
def adminhome():
   print("[Info]")
   return render_template('adminhome.html')

@app.route('/admin.html')
def admin():
   return render_template('admin.html')


@app.route('/prevention.html')
def prevention():
   return render_template('prevention.html')

@app.route('/upload.html')
def upload():
   return render_template('upload.html')

@app.route('/upload_chest.html')
def upload_chest():
   return render_template('upload_chest.html')


@app.route('/upload_ct.html')
def upload_ct():
   return render_template('upload_ct.html')

if __name__ == '__main__':
	app.run(debug = True)
