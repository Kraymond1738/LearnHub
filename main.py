#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from engine.db_config import SQLALCHEMY_DATABASE_URI
from engine.db_mod import add_user
from engine.database import db, User


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'learnhub'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

#Route for home
@app.route('/')
def landing():
    return render_template('html/landing.html')

#route for home page
@app.route('/home')
def home():
    return render_template('html/Home.html')

#route for about page
@app.route('/about')
def about():
    return render_template('html/About.html')

#route for contact page
@app.route('/contact')
def contact():
    return render_template('html/contact.html')

#route for the courses page
@app.route('/courses')
def courses():
    return render_template('html/courses.html')

#route for blog
@app.route('/blog')
def blog():
    return render_template('html/Blog.html')


# Routes for authentication

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        phone_number = request.form.get('phone_number')
        account_type = request.form.get('account_type')

        #check if theres already an account using the provided email
        exist = User.query.filter_by(email=email).first()
        if exist:
            flash("Email already exists", 'error')
            return redirect('/login')

        # Hash the password before storing it in the database
        print("pass", request.form)
        hashed_password = generate_password_hash(str(password))

        # Create a new User object
        user = User(first_name=(first_name), last_name=last_name, email=email,
                    password=hashed_password, phone_number=phone_number, account_type=account_type)

        # Add the user to the database
        add_user(user)

        return redirect('/login')

    return render_template('html/signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Query the user with the provided email
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            # User is authenticated, store user ID in the session
            session['user_id'] = user.id
            return redirect('/dashboard')
        else:
            # Invalid credentials, display an error message
            #error_message = 'Invalid email or password'
            #return render_template('login.html', error_message=error_message)
            pass

    return render_template('html/login.html')

@app.route('/logout')
def logout():
    # Clear the user ID from the session
    session.pop('user_id', None)
    return redirect('/login')

# Other routes and views

@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in
    if 'user_id' not in session:
        return redirect('/login')

    # Retrieve the user from the database
    user = User.query.get(session['user_id'])

    return render_template('html/dashboard.html', user=user)

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
