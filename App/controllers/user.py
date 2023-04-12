from App.models import User, UserData, UserPreferences
from App.database import db
import os
from flask import Flask, jsonify, request, render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from App.models import db, User

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/login', methods=['GET'])
def login_page():
  return render_template('login.html')


@app.route('/app', methods=['GET'])
@login_required
def todos_page():
  userData = UserData.query.filter_by(user_id=current_user.id).all()
  return render_template('index.html', userData = userData)

@app.route('/signup', methods=['GET'])
def signup_page():
  return render_template('signup.html')

#action routes

@app.route('/signup', methods=['POST'])
def signup_action():
  data = request.form  # get data from form submission
  newuser = User(username=data['username'], email=data['email'], password=data['password'], dateOfBirth = data['dateOfBirth'], height = data['height'],weight = data['weight'],sex = data['sex'])
  try:
    db.session.add(newuser)
    db.session.commit()  # save user
    login_user(newuser)  # login the user
    flash('Account Created!')  # send message
    return redirect('layout.html')  # redirect to homepage
  except Exception:  # attempted to insert a duplicate user
    db.session.rollback()
    flash("username or email already exists")  # error message
  return redirect(url_for('layout.html'))

@app.route('/login', methods=['POST'])
def login_action():
  data = request.form
  user = User.query.filter_by(username=data['username']).first()
  if user and user.check_password(data['password']):  # check credentials
    flash('Logged in successfully.')  # send message to next page
    login_user(user)  # login the user
    return redirect('/app')  # redirect to main page if login successful
  else:
    flash('Invalid username or password')  # send message to next page
  return redirect('/')

@app.route('/logout', methods=['GET'])
@login_required
def logout_action():
  logout_user()
  flash('Logged Out')
  return redirect(url_for('login_page'))





















def create_user(username, password, email,dateOfBirth,height,weight,sex):
    newuser = User(username=username, password=password,email = email,dateOfBirth = dateOfBirth,height = height,weight = weight,sex = sex)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user_by_email(email):
    return User.query.filter_by(email = email).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username, email,dateOfBirth,height,weight,sex):
    user = get_user(id)
    if user:
        user.username = username
        user.email = email
        user.dateOfBirth = dateOfBirth
        user.height = height
        user.weight = weight
        user.sex = sex
        db.session.add(user)
        return db.session.commit()
    return None
    