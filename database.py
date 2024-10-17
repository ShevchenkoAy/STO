import sqlite3

conn = sqlite3.connect('database.db')

cur = conn.execute('''CREATE TABLE IF NOT EXISTS comments(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
brand TEXT NOT NULL,
comment TEXT NOT NULL,
good TEXT NOT NULL,
bad TEXT NOT NULL,
evaluation INTEGER NOT NULL
                  )''')



conn.commit()
conn.close()



def add_comments(name, brand, comment, good, bad, evaluation):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO comments (name, brand, comment, good, bad, evaluation)
                   VALUES (?, ?, ?, ?, ?, ?)''', (name, brand, comment, good, bad, evaluation))
    conn.commit()
    conn.close()

def view_comments():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    comments = cur.execute('''SELECT * FROM comments''').fetchall()
    conn.close()
    return comments

def view_comment(id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    comment = cur.execute('''SELECT * FROM comments WHERE id=?''',
                          (id,)).fetchone()
    conn.close()
    return comment
