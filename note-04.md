# `04` Install and Test a Login Application

## Build the database

Create a database with the name example.db

Run the script login-database.py and follow the menu options to create a database (C) followed by displaying all the data (S).

## Run the Flask application

Rename the file app-login.py to app.py, then rund the flask application with the command.

```
python -m flask run
```

Open the web browser and select the menu to register a user. Next, click to login.

Observer the results at the command line.

Create the pages for success and failed user login.

## Create a page that have a session for a valid login

Implement the index page to have a user session. Here is an example of using a Flask session.

```
from flask import Flask, render_template, redirect, request, session
from flask_session import Session

app = Flask(__name__)


app.config["SESSION_PERMANENT"] = False     # Sessions expire when the browser is closed
app.config["SESSION_TYPE"] = "filesystem"     # Store session data in files
# Initialize Flask-Session
Session(app)
```

The routes can be implemented. Example
```
@app.route("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
```