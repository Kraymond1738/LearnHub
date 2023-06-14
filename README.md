# LearnHub E-Learning Web Application

<a href="https://kriztech.github.io">
    <img src="/static/images/learnhub_logo.png" alt="LearnHub" title="LearnHub">
</a>

[LearnHub](https://kriztech.github.io) is an innovative course provider app that offers a wide range of educational programs to enhance your knowledge and skills.
With a userinterface, LearnHub provides interactive courses, expert instructors, webinars and personalized learning paths.
Whether you are interested in professional development, academic subjects, or hobbies, LearnHub has something for everyone. LearnHub is an online platform that creates teaching and learning environments for users to engage and interact.

## Table of content

- [The Story](#the-story)
- [Getting Started](#getting-started)
- [Screenshots](#screenshots)
- [Features](#features)
    - [Github OAuth](#github-oauth)
    - [Job Search](#job-search)
    - [Add Applied](#add-applied)
    - [Applied Jobs](#applied-jobs)
    - [Rewards](#rewards)
- [Built With](#built-with)
- [API](#api)
- [Future](#future)
- [Authors](#authors)
    - [Christopher Choe](#christopher-choe)
    - [Susan Su](#susan-su)
- [Acknowledgments](#acknowledgements)

## The Story

First, We are passionate about fostering a love for learning and empowering individuals to reach their full potential. We believe that education should be accessible to everyone, which is why we offer a diverse range of online courses in various subjects and disciplines. Our platform is designed to provide a seamless learning experience, with interactive lessons, engaging content, and expert instructors. Whether you're looking to enhance your professional skills, explore new hobbies, or pursue academic interests, LearnHub is here to support you on your learning journey. Join our vibrant community of learners and embark on a path of continuous growth and discovery

That is why we are LearnHub!

A workspace was created on Trello which was utilized throughout in order to keep tasks and communication organized.
The javascript front end and the way the dashboard was designed, allowed learnHub to have more dynamic features with a tutor creating a course and a student being able to enroll for a course without distorting the rest of the project.
A REST API allowed for this frontend to interact with the backend in a simple and well documented way.
We decided to use ORM and MySQL because of modularity and familiarity.

Front End
* Javascript components
* CSS for consistent styling
* API Calls to manipulate database

REST API
* GET, POST, PUT requests handled

Relational Database
* Handled with ORM (SQLAlchemy)
* Model system with base model handling identification
* Many to many relationship for users.

Server / Deployment
* Nginx / Gunicorn / Flask
* AWS EC2 on Ubuntu 20.04

## Getting Started

Access it on learnnhub.com and create an account today!
* To explore features without logging in, check out [Features](#features)

## Screenshots

<img width=50% src="/static/images/Screenshot (21).png">

<img width=50% src="/static/images/Screenshot (12).png">

<img width=50% src="/static/images/Screenshot (3).png">

## Features

LearnHub has features that can be found through our dropdown navigation bar menu.

<img width=50% src="/static/images/Screenshot (8).png">

These features will be explored below!

<img width=50% src="/static/images/Screenshot_2.png">

### **Tutor Dashboard**

When a Tutor creates an account and log's in with the tutor account type, The tutor has the features of creating a content, managing the content and also starting a live session.

<img width=50% src="Screenshot (6).png">

### **Student Dashboard**

The Student dashboard webpage allows a student the featured ability to view courses in cart, enroll for courses, get access to materials and also join live discussions and meetups.

<img width=75% src="/static/images/Screenshot (5).png">

<img width=75% src="/static/images/Screenshot (20).png">


This page gives a view of all our distinguished and prestigious tutors

<img width=75% src="/static/images/Screenshot (4).png">


### **Rewards**

Upon successful completion of a certificate program, learners receive a recognized certificate, showcasing their newly acquired skills and knowledge. This certification from LearnHub serves as a valuable credential, validating one's expertise to employers and professional networks.Overall, LearnHub's certificate programs offer a convenient and reputable way to upskill or reskill, empowering individuals to thrive in today's rapidly evolving job market.

<img width=75% src="/Screenshot (24).png">

## Built With
* [Python](http://www.python.org) - The Backend Language
* [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - The Frontend Language
* [Flask](http://flask.pocoo.org/docs/1.0/) - The Web Development Framework
* [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL Toolkit and Object Relational Mapper
* [MySQL](https://mysql.com) - Relational Database Management System
* [Material UI](https://material-ui.com) - Pre-Built React components

## API

/api/user

/api/user/<user_id>/email

GET: Returns a user email
POST: Adds a user email

## Future

There are plenty of features that we would love to implement into LearnHub.
The programs cover a vast array of subjects, including business, technology, healthcare, creative arts, and more. Learners can choose programs based on their interests and career goals, allowing them to acquire valuable expertise and stay competitive in their chosen fields. For a better comparative advantage, we're looking at adding virtual features to learnhub to give our users a first-hand live sessions with tutors. This will be an added feature in future because implementing a complete and secure live session solution involves more complex technologies and considerations such as video encoding, streaming protocols, authentication, and encryption. It is recommended to use specialized frameworks or libraries to ensure a robust and secure implementation.

If you have any suggestions or would like to contribute to LearnHub, please contact either of us.

## Authors
### **Christian Donatus**
[Christian](https://KrizTech.github.io)

Christian (KrizTech) is a Frontend software engineer, working on the system design, interface, technical writing and taking charge of the styling and javascript portion of LearnHub while still partially involved in the backend database and debugging of bugs.

### **Kazumba Raymond**
[Kazumba](https://Kraymond1738.github.io)

Kazumba is a backend software engineer, working on the system backend, database, and REST API for the most part with some fingerprints in the frontend in order to better understand and integrate the backend into the whole picture.

### **Afolabi Seyi**

Afolabi is a frontend software Engineer, works on the design and writeups computation.Passionate about the physical appearance of the site and engagement of the user with the interface.
[Afolabi](https://Afooseyi.github.io)
If you would like to contact [Kazumba](https://Kraymond1738.github.io/) or [Chris](https://KrizTech.github.io) or [Afolabi](https://Afooseyi.github.io/) about any opportunities, feel free to reach out!


## Acknowledgements
* [ALX School](https://www.alx.com/) (Staff and Students)
* Fellow LearnHub Team Mates
* ALx Peers
