import sqlite3

def init_con():
    con = None
    try:
        con = sqlite3.connect("users.db")
        con = sqlite3.connect("news.db")
        print("connection OK")
    except Exception:
        print("failed")
    return con

def init_table_users():
    connection = init_con()
    sql_users = "CREATE TABLE IF NOT EXISTS users(name TEXT)"
    connection.execute(sql_users)
    connection.commit()
    connection.close()

def init_table_news():
    connection = init_con()
    sql_mews = "CREATE TABLE IF NOT EXISTS news(name TEXT, title TEXT, content TEXT, date FLOAT)"
    connection.execute(sql_mews)
    connection.commit()
    connection.close()

def verification(username):
    connection = init_con()
    cur = connection.cursor()
    check = cur.execute("SELECT name FROM users WHERE name = ?", (username, ))
    user = check.fetchone()
    if user is None:
        return None
    else: 
        return user


def add_news(username, title, content, date):
    connection = init_con()
    cur = connection.cursor()
    cur.execute("INSERT INTO news(name, title, content, date) VALUES(?, ?, ?, ?)", (username, title, content, date,))
    connection.commit()
    connection.close()


def read_news():
    connection = init_con()
    connection.row_factory = sqlite3.Row
    cur = connection.cursor()
    cur.execute("SELECT * FROM news")
    rows = cur.fetchall()
    connection.close()
    return rows

