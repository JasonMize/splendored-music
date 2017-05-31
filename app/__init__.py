from flask import Flask
from flask.ext.scss import Scss

app = Flask(__name__)
Scss(app, static_dir='static', asset_dir='assets')

from app import views
from app import filters

