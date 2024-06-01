from flask import Flask, render_template, session, flash, redirect, url_for, request
from functools import wraps
import paramiko

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this to a random secret key

# Simple user database
users = {
    'luck': 'plaplifetime1',
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

def sftp_connect():
    try:
        transport = paramiko.Transport(('townside.sharp.host', 2022))
        transport.connect(username='sajmfe8f.c4228b5c', password='Archie0916$')
        sftp = paramiko.SFTPClient.from_transport(transport)
        return sftp
    except Exception as e:
        print(f"Error connecting to SFTP: {e}")
        return None

def get_file_content(file_name):
    sftp = sftp_connect()
    if not sftp:
        return None
    try:
        with sftp.file(f'/Pavlov/Saved/Config/{file_name}', 'r') as file:
            content = file.read().decode()
        sftp.close()
        return content
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error fetching file content: {e}")
        return None

def update_file_content(file_name, new_content):
    sftp = sftp_connect()
    if not sftp:
        return False, "Error connecting to SFTP"
    try:
        with sftp.file(f'/Pavlov/Saved/Config/{file_name}', 'w') as file:
            file.write(new_content.encode())
        sftp.close()
        return True, 'File updated successfully!'
    except Exception as e:
        print(f"Error updating file content: {e}")
        return False, str(e)

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
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html', content='', users=users, file_name='')

@app.route('/get-file', methods=['POST'])
@login_required
def get_file():
    if request.method == 'POST':
        file_name = request.form['file_name']
        file_content = get_file_content(file_name)
        if file_content is not None:
            flash(f"Contents of {file_name} loaded successfully.", 'success')
            return render_template('home.html', content=file_content, users=users, file_name=file_name)
        else:
            flash(f"File '{file_name}' not found or error occurred.", 'danger')
    return redirect(url_for('home'))

@app.route('/update-file', methods=['POST'])
@login_required
def update_file():
    if request.method == 'POST':
        file_name = request.form['file_name_update']
        new_content = request.form['new_content']
        success, message = update_file_content(file_name, new_content)
        if success:
            flash(message, 'success')
        else:
            flash(message, 'danger')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
