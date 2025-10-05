from datetime import datetime

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    return "Hello, Flask! Its " + formatted_now