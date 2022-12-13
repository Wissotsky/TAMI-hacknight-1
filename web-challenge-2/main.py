import base64
import random
from flask import Flask, make_response, render_template, request, redirect, url_for
import sqlite3
import libinjection

app = Flask(__name__)

def is_sqli(inp_str) -> bool:
    """Check if the string is a SQL injection"""
    out_tuple = libinjection.is_sql_injection(inp_str)
    if out_tuple['is_sqli'] == True:
        return True
    else:
        return False

def sqlescape(str):
    return str.translate(
        str.maketrans({
            "\0": "\\0",
            "\r": "\\r",
            "\x08": "\\b",
            "\x09": "\\t",
            "\x1a": "\\z",
            "\n": "\\n",
            "\r": "\\r",
            "\"": "",
            "'": "",
            "\\": "\\\\",
            "%": "\\%"
        }))

# main page that is a twitter clone with anonymous posting by choosing a username
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO messages (username, message) VALUES (?, ?)", (username, message))
        conn.commit()
        conn.close()
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('username', base64.urlsafe_b64encode(sqlescape(username).encode('utf8')).decode('utf8'))
        return resp
    else:
        if request.cookies.get('username') is None or is_sqli(request.cookies.get('username')):
            username = f"RandomNoob{random.randint(1000, 9999)}"
        else:
            username = base64.urlsafe_b64decode(request.cookies.get('username')).decode('utf8')
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(f"""SELECT *,
                        CASE WHEN username == '{username}' 
                        THEN true
                        ELSE false 
                        END AS style
                    FROM messages ORDER BY created_at DESC""")
        messages = c.fetchall()
        conn.close()
        print(messages)
        # render template with messages and username stored in cookie
        return render_template('index.html', messages=messages, username=username)