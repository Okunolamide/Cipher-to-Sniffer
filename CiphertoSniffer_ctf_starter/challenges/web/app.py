from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os

# *** INTENTIONAL VULNERABILITY FOR CTF ONLY ***
# This app is for local, educational use. Do NOT deploy to the public internet.

DB_PATH = os.path.join(os.path.dirname(__file__), "site.db")
FLAG = "FLAG{SQL_INJECTION_MASTER}"

app = Flask(__name__)

def init_db():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT);")
        c.execute("INSERT INTO users (username, password) VALUES ('admin', 'password');")
        c.execute("INSERT INTO users (username, password) VALUES ('guest', 'guest');")
        conn.commit()
        conn.close()

@app.route("/", methods=["GET"])
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    # INTENTIONALLY vulnerable SQL string concatenation (for CTF)
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute(query)
        row = c.fetchone()
    except Exception as e:
        row = None
    finally:
        conn.close()

    if row:
        return render_template("admin.html", flag=FLAG, user=row[1])
    else:
        return render_template("login.html", error="Invalid credentials.")

if __name__ == "__main__":
    init_db()
    # Bind only to localhost
    app.run(host="127.0.0.1", port=5000, debug=False)
