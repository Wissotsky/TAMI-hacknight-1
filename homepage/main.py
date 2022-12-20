from flask import Flask, make_response, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# read ipv4 from env variable local_ipv4
local_ipv4 = os.environ['local_ipv4']
# just serve index.html
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', local_ipv4=local_ipv4)