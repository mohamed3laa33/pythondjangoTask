from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, app, url_for
from datetime import timedelta
import os

from flask import Flask, render_template, request, redirect, flash, url_for
from werkzeug import secure_filename


app = Flask(__name__)
UPLOAD_FOLDER = '/home/seb/digizilla/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

@app.route('/')
def home():
    flash('Username and password don\'t match!')
    if not session.get('succesful_login'):
        return render_template('index.html')
    else:
        return redirect(url_for('upload_page'))

@app.route('/login', methods = ['GET', 'POST'])
def do_user_login():
    if request.form['username'] == 'a' and request.form['password'] == 'p':
        session['succesful_login'] = True
        app.permanent_session_lifetime = timedelta(seconds=5)
    else:
        flash('Username and password don\'t match!')
    return home()

# @app.route('/login2', methods = ['GET', 'POST'])
# def login_page():
#     error=''
#     try:
#         if request.method == "POST":
#             u = request.form['username'] 
#             p = request.form['password']
#             flash(u, p)
#             if u == 'a' and p == 'p':
#                 # session['succesful_login'] = True
#                 # app.permanent_session_lifetime = timedelta(seconds=5)
#                 return redirect(url_for('/upload_page'))
#             else:
#                 flash('Username and password don\'t match!')
#         return render_template('index.html')
#     except Exception as e:
#         flash(e)
#         return render_template('index.html')


@app.route('/upload/', methods = ['GET', 'POST'])
def upload_page():
    return render_template('upload.html')

@app.route('/uploading/', methods = ['GET', 'POST'])
def upload_file():
    # # flash('file uploaded successfully!')
    if request.method == 'POST':
        f = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            # f.save(secure_filename(f.filename))
            # flash('file uploaded successfully!')
            return redirect(url_for('upload_page'))
    return render_template('login2.html')
    # flash('file uploaded successfully!')


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)





