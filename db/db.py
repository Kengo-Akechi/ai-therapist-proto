import sqlite3

def init_db():
    conn = sqlite3.connect("chat_history.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, user TEXT, message TEXT)''')
    conn.commit()
    conn.close()

def save_message(user, message):
    conn = sqlite3.connect("chat_history.db")
    c = conn.cursor()
    c.execute("INSERT INTO messages (user, message) VALUES (?, ?)", (user, message))
    conn.commit()
    conn.close()
