import sqlite3
from flask import Flask, render_template, request, redirect, url_for, g
from datetime import datetime

app = Flask(__name__)
DATABASE = "example.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']
        email = request.form['email']
        # Here, you would typically store the user data in a database
        if password == password2:
            
            with get_db() as db:
                try:
                    current_datetime = datetime.now()
                    cur = get_db().cursor()
                    cur.execute("INSERT INTO users (username, password, email, registration_date) VALUES (?, ?, ?, ?)", (username, password, email, current_datetime))
                    db.commit()
                    return redirect(url_for('success', username=username))
                except sqlite3.IntegrityError :
                    db.rollback()
                    return "Duplicate data for registration "
                except Exception as e:
                    db.rollback()
                    return "Unknown error saving to database " + e
        return redirect(url_for('nosuccess', username=username))
    return render_template('registration.html')

@app.route('/success')
def success():
    message = request.args.get('username')
    return message + " Registration Successful!"

@app.route('/nosuccess/<username>')
def nosuccess(username):    
    return render_template('registration_failed.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['userName']
        password = request.form['password']
        check_email(username, password)
        return "Login attempted!"
    return render_template('login.html')
if __name__ == '__main__':
    app.run(debug=True)

def check_email(email, password):    
    conn = sqlite3.connect('example.db')  # Creates a new database file if it doesn’t exist
    cursor = conn.cursor()
    try:
        # Query data
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,) )
        row = cursor.fetchone()
        user_email = row[2]
        print("Found " + user_email)
        if row[3] == password:
            print("Login success")
        else:
            print("Failed login")
    except sqlite3.Error as e:
        print(f"Error reading table: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()