from flask import Flask, make_response, render_template, request, redirect, url_for

app = Flask(__name__)

comments = []

# simple blogpost with comments section (no login required)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # get the comment from the form
        comment = request.form['comment']
        # if the comment includes a script tag
        if '<script>' in comment:
            # intersperse the comment with zero-width spaces
            comment = ''.join([c + '\u200b' for c in comment])
        # add the comment to the list
        comments.append(comment)
        # redirect to the index page
        return redirect(url_for('index'))

    # render the index page with the comments
    return render_template('index.html', comments=comments)