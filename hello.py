import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World from india!</p>"
    #message = os.getenv("CUSTOM_MESSAGE", "Thanks, Ashu!")
    #return f"<p>{message}</p>"
    

@app.route('/adm')
def admin():
    return "This is the Admin Page"
