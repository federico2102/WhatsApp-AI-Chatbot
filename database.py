import sqlite3


def create_table():
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone_number TEXT,
            text_author TEXT,
            timestamp TEXT,
            message TEXT
        )
    ''')

    conn.commit()
    conn.close()


def insert_message(phone_number, text_author, timestamp, message):
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO messages (phone_number, text_author, timestamp, message)
        VALUES (?, ?, ?, ?)
    ''', (phone_number, text_author, timestamp, message))
    conn.commit()
    conn.close()


def retrieve_chat_history(phone_number):
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM messages WHERE phone_number = ? ORDER BY timestamp",
        (phone_number,)
    )
    chat_history = cursor.fetchall()
    conn.close()
    return chat_history


def delete_oldest_messages(phone_number):
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM messages WHERE id IN (
            SELECT id FROM messages WHERE phone_number = ?
            ORDER BY timestamp ASC LIMIT 2
        )
    """, (phone_number,))
    conn.commit()
    conn.close()
