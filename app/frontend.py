from app import app
from flask import render_template, request, session, redirect

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html', message='Oops! Looks like you\'ve come to the wrong page ')

@app.route('/')
def index_post():
    return render_template('index.html',message='')

@app.route('/', methods=['POST'])
def index():
    fname = request.form.get('fname')
    return render_template('index.html',message=fname)