import os
from flask import Flask, render_template
# from flask.ext import assets
# from flask.ext.scss import Scss

app = Flask(__name__)
# Scss(app, static_dir='static', asset_dir='assets')

from app import views
from app import filters


