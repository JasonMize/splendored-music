# import sys
 
# from app import app 
from flask import * 

application = Flask(__name__)

# app = Flask(__name__)
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    # application.debug = True
    application.run()
