from flask import Flask, make_response, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# login page with get and post options
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # connect to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # unsafely concatenate the username and password into a sql query
        print("SELECT uid FROM users WHERE username = '" + username + "' AND password = '" + password + "'")
        cursor.execute("SELECT uid FROM users WHERE username = '" + username + "' AND password = '" + password + "'")
        user = cursor.fetchone()
        print(user)

        if not user:
            return redirect(url_for('index'))
        if user[0] == "YouWin":
            resp = make_response(redirect(url_for('you_win')))
            resp.set_cookie('uid', "YouWon")
            return resp
        # if the user does not exist, redirect to the login page
        else:
            return redirect(url_for('index'))

    # if the user is not logged in show the login page
    return render_template('loginpage.html')

# win page
@app.route('/you_win')
def you_win():
    # if the user is logged in show the win page
    if request.cookies.get('uid') == "YouWon":
        return "<h1>You completed the first challenge successfully</h1>"
    # if the user is not logged in redirect to the login page
    else:
        return redirect(url_for('index'))