from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import os
import requests

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this to a random secret key

# Define the URL to fetch the mod.txt file from your Pavlov VR server
MOD_URL = 'http://your_pavlov_server/mod.txt'  # Replace 'your_pavlov_server' with the actual URL

# Simple user database
users = {
    'luck': 'plaplifetime1',  # username: password (for demonstration purposes)
    'srwinter': 'gibbythebest',
    'user2': 'password2',
    'user3': 'password3'
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['logged_in'] = True
            session['username'] = username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))  # Redirect to home page on successful login
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

@app.route('/home')
@login_required
def home():
    content = ''
    if 'logged_in' in session:
        try:
            response = requests.get(MOD_URL)
            if response.status_code == 200:
                content = response.text
            else:
                flash(f'Failed to fetch mod.txt: {response.status_code}', 'danger')
        except Exception as e:
            flash(f'Error fetching mod.txt: {e}', 'danger')
    return render_template('home.html', content=content, users=users)

if __name__ == '__main__':
    app.run(debug=True)
