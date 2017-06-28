import sys
 
from app import app
# from flask import Flask 

# app = Flask(__name__)
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    # application.debug = True
    app.run()
