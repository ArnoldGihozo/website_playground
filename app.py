import flask
from flask import Flask, Response, render_template, url_for

app = Flask(__name__)

@app.route('/')
def hello():
   return render_template("index.html")