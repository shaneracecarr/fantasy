from flask import Flask, render_template, request, jsonify, session, redirect, url_for

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key'  # Use a secure key in production

# Route for the login page
@app.route('/')
def login_page():
    return render_template('login.html')  # Render the login page

# Route to handle login form submission
@app.route('/login', methods=['POST'])
def login():
    # Get form data
    username = request.form['username']
    password = request.form['password']

    # Hardcoded login validation (you can modify this later to check against a database)
    if username == "shaneracecarr" and password == "password123":
        session['user'] = username  # Store the username in the session
        return redirect(url_for('dashboard'))  # Redirect to the dashboard
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Route for the dashboard page (protected by session)
@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in (i.e., if 'user' is in session)
    if 'user' in session:
        return render_template('dashboard.html', username=session['user'])  # Pass the username to the dashboard
    else:
        return redirect(url_for('login_page'))  # Redirect to login if not logged in

if __name__ == "__main__":
    app.run(debug=True)
