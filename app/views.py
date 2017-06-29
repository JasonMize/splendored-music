import os
 
from flask import render_template
 
from app import application
 
@application.route("/")
@application.route("/index")
def index():
    return render_template("includes/index.html")

@application.route("/about")
def about():
    return render_template("includes/about.html")