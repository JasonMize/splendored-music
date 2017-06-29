from flask import render_template
from app import app
 

@app.route("/")
@app.route("/index")
def index():
    return render_template("includes/index.html")

@app.route("/about")
def about():
    return render_template("includes/about.html")

