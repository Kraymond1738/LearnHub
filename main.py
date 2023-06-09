#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from engine.db_config import SQLALCHEMY_DATABASE_URI
from engine.db_mod import *
from engine.database import db, User
import json


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
            
            #check the account type
            acc_type = user.account_type
            if acc_type== 'Tutor':
                return redirect('/tutor_dashboard')
            else:
                return redirect('/student_dashboard')
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


#dashboard routes

@app.route('/tutor_dashboard', methods=['GET'])
def tutor_dashboard():
    # Check if the user is logged in
    if 'user_id' not in session:
        return redirect('/login')

    # Retrieve the user from the database
    user = User.query.get(session['user_id'])

    courses = Course.query.filter_by(tutor_id=user.id).all()
    dict_courses = []
    for course in courses:
        course_data = {
            'title': course.title,
            'description': course.description,
            'course_content': course.course_content,
        }
        dict_courses.append(course_data)

    return render_template('html/tutor_dashboard.html', user=user.first_name, courses=dict_courses)

@app.route('/student_dashboard')
def student_dashboard():
    # Check if the user is logged in
    if 'user_id' not in session:
        return redirect('/login')

    # Retrieve the user from the database
    user = User.query.get(session['user_id'])
    return render_template('html/student_dashboard.html', user=user.first_name)

#tutors page
@app.route('/tutors')
def tutors():
    return render_template('html/tutors.html')

#view_courses page
@app.route('/view_courses')
def view_courses():
    return render_template('html/view_courses.html')

#create_content page
@app.route('/create_content', methods=['GET', 'POST'])
def create_content():
    if request.method=='POST':
        title = request.form.get('course_title')
        description = request.form.get('course_description')
        course_content = request.form.get('course_content')
        
        tutor_id = session['user_id']

        #create a new course object

        new_course = Course(title=title, description=description,
                        course_content=course_content,tutor_id=tutor_id)

        add_course(new_course)
        return redirect('tutor_dashboard')
    
    return render_template('html/create_content.html')

#manage_content page
@app.route('/manage_content', methods=['GET', 'POST'])
def manage_content():
    if request.method == 'POST':
        action = request.form.get('action')
        course_id = request.form.get('course_id')

        if action == 'update':
            title = request.form.get('title')
            description = request.form.get('description')
            course_content = request.form.get('course_content')

            course = Course.query.get(course_id)
            if course:
                course.title = title
                course.description = description
                course.course_content = course_content
                db.session.commit()

        elif action == 'delete':
            course = Course.query.get(course_id)
            if course:
                db.session.delete(course)
                db.session.commit()

        return redirect('/manage_content')

    user = User.query.get(session['user_id'])
    courses = Course.query.filter_by(tutor_id=user.id).all()

    return render_template('html/manage_content.html', courses=courses)



    user = User.query.get(session['user_id'])

    courses = Course.query.filter_by(tutor_id=user.id).all()
    dict_courses = []
    for course in courses:
        course_data = {
            'course_id':course.id,
            'title': course.title,
            'description': course.description,
            'course_content': course.course_content,
        }
        dict_courses.append(course_data)

    return render_template('html/manage_content.html',courses=dict_courses)

#live_session page
@app.route('/live_session')
def live_session():
    return render_template('html/video.html')

#enrollment page
@app.route('/enroll')
def enroll():
    return render_template('html/enroll.html')

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
