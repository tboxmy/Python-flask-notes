# `02` Common packages

General packages to work with 

## os

Check access to the current working directory

Create a new file called example_os.py

```
import os 
cwd = os.getcwd() 
print("Current working directory:", cwd) 
```

Click the Run button in Visual Code and view results in the terminal window.

## datetime

Handle date and time objects.

Create a new file called example_datetime.py

```
from datetime import datetime

now = datetime.now()
formatted_now = now.strftime("%A, %d %B, %Y at %X")
print("Hello, Flask! Its ", formatted_now)
```

## sqlite3

SQLite3 is available in Python as a SQL compliant database that is serverless. 

Refer to the example file example-sqlite.py

1. Connect to a database

```
import sqlite3

def open_database():
    conn = sqlite3.connect('example.db')  t
    cursor = conn.cursor()
```

2. Create a table

Create a table name **users** with the columns

- id as integer
- username as text
- email as varchar(100), not null and is unique
- password as text
- registration_date as timestamp
- is_verified as integer that defaults to zero

Always close a connections upon completion of a task.

```
import sqlite3

def create_database():
    conn = sqlite3.connect('example.db')  t
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,       
            email VARCHAR(100) NOT NULL UNIQUE,
            password TEXT,
            registration_date TIMESTAMP, 
            is_verified INT DEFAULT 0
        )
    ''')
    conn.close()
```

3. Insert a row of data

Here is an example to insert a row into an existing database.

```
import sqlite3

def insert_database():
    conn = sqlite3.connect('example.db')  t
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password, email, registration_date) VALUES (?, ?, ?, ?)", ('manager', 'Sales Manager', 'sales.manager@example.com', current_datetime))
    conn.commit()  # or conn.rollback() if something fails
    conn.close()
    print(f"Success")
```

4. Selecting data

Example to retrieve the first 10 results from the database.

```
import sqlite3
def retrieve_users():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    try:
        # Query data
        cursor.execute("SELECT * FROM users limit 10")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Error reading table: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()
```

