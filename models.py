import sqlite3

def save_form_data(name, message, email):
    print(name, message, email)

    # connecting to database, and setting up code variables
    conn = sqlite3.connect('Database.db')  # Connecting or creating a database from filepath
    cursor = conn.cursor() # not needed, but for better code

    # creates table for submissons
    cursor.execute('''CREATE TABLE IF NOT EXISTS submissons (
                        name TEXT NOT NULL,
                        message TEXT NOT NULL,
                        email TEXT NOT NULL
                    )''')

    # inserting and then commiting new data
    cursor.execute("INSERT INTO submissons (name, message, email) VALUES (?, ?, ?)", (str(name), str(message), str(email)))
    conn.commit()  # Commit changes to the database
