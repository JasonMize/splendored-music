from flask import * 

application = Flask(__name__)
app = application

from app import app
 
if __name__ == "__main__":
    app.run()
