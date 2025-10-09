import sqlite3
from datetime import datetime

def welcome():
    print("Your command [C, S, or a user ID]?")
    respond = input()
    if respond == "C":
        create_database()
    elif respond == "S":
        retrieve_users()
    else:
        try:
            int_id = int(respond)
            retrieve_user(int_id)
        except ValueError:
            print("#101 Invalid user ID")
        

def create_database():
    conn = sqlite3.connect('example.db')  # Creates a new database file if it doesn’t exist
    cursor = conn.cursor()
    # Create a table
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
    conn.execute("BEGIN")
    current_datetime = datetime.now()
    # Insert data
    cursor.execute("INSERT INTO users (username, password, email, registration_date) VALUES (?, ?, ?, ?)", ('manager', 'Sales Manager', 'sales.manager@example.com', current_datetime))
    cursor.execute("INSERT INTO users (username, password, email, registration_date) VALUES (?, ?, ?, ?)", ('sales1', 'Sales', 'sales1@example.com', current_datetime))
    cursor.execute("INSERT INTO users (username, password, email, registration_date) VALUES (?, ?, ?, ?)", ('sales2', 'Sales', 'sales2@example.com', current_datetime))
    # perform database operations
    conn.commit()  # or conn.rollback() if something fails
    conn.close()
    print(f"Success")

def retrieve_users():
    conn = sqlite3.connect('example.db')  # Creates a new database file if it doesn’t exist
    cursor = conn.cursor()
    try:
        # Query data
        cursor.execute("SELECT * FROM users WHERE password IS NOT NULL")
        rows = cursor.fetchall()
        for row in rows:
            print(row[0])
            print(row)
    except sqlite3.Error as e:
        print(f"Error reading table: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()

def retrieve_user(id):
    print(f"Type of the argument: {type(id)}")
    conn = sqlite3.connect('example.db')  # Creates a new database file if it doesn’t exist
    cursor = conn.cursor()
    try:
        # Query data
        cursor.execute("SELECT * FROM users WHERE id = ?", (id,) )
        row = cursor.fetchone()
        user_email = row[2]
        print("Found " + user_email)
        print(row)
    except sqlite3.Error as e:
        print(f"Error reading table: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()

def delete_users_table(database_name):
    conn = None
    table_name = "users"
    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        # SQL statement to drop the table
        # IF EXISTS is optional but prevents an error if the table does not exist
        sql_statement = f"DROP TABLE IF EXISTS {table_name};"

        cursor.execute(sql_statement)
        conn.commit()
        print(f"Table '{table_name}' deleted successfully from '{database_name}'.")

    except sqlite3.Error as e:
        print(f"Error deleting table: {e}")
    finally:
        if conn:
            conn.close()

welcome()
#delete_users_table("example.db")