from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user
from App.models import User
from.index import index_views
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from App.controllers import (
    create_user,
    logout_user_action,
    login_user,
    authenticate, 
    rollback,
    get_all_users,
    get_all_users_json,
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/users', methods=['GET'])
@login_required
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users, current_user = current_user)

@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    create_user(username=data['username'], email=data['email'], password=data['password'], dateOfBirth = data['dateOfBirth'], height = data['height'],weight = data['weight'],sex = data['sex'])
    return jsonify({'message': f"user {data['username']} created"})

@user_views.route('/api/login', methods=['POST'])
def user_login_api():
  data = request.json
  token = authenticate(data['username'], data['password'])
  if not token:
    return jsonify(message='bad username or password given'), 401
  return jsonify(access_token=token)

@user_views.route('/api/identify', methods=['GET'])
@jwt_required()
def identify_user_action():
    return jsonify({'message': f"username: {current_user.username}, id : {current_user.id}"})

@user_views.route('/users', methods=['POST'])
def create_user_action():
    data = request.form
    flash(f"User {data['username']} created!")
    create_user(username=data['username'], email=data['email'], password=data['password'], dateOfBirth = data['dateOfBirth'], height = data['height'],weight = data['weight'],sex = data['sex'])
    return redirect(url_for('user_views.get_user_page'))

@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')


@user_views.route('/signup', methods=['GET'])
def signup_page():
  return render_template('signup.html')

@user_views.route('/login', methods=['GET'])
def login_page():
  return render_template('login.html')


# action routes

@user_views.route('/login', methods=['POST'])
def login_action():
  data = request.form
  user = User.query.filter_by(username=data['username']).first()
  if user and user.check_password(data['password']):  # check credentials
    flash('Logged in successfully.')  # send message to next page
    login_user(user,False)  # login the user
    return redirect('/users')  # redirect to main page if login successful
  else:
    flash('Invalid username or password')  # send message to next page
  return redirect('/')


@user_views.route('/signup', methods=['POST'])
def signup_action():
  try:
    data = request.form  # get data from form submission
    newuser =create_user(username=data['username'], email=data['email'], password=data['password'], dateOfBirth = data['dateOfBirth'], height = data['height'],weight = data['weight'],sex = data['sex'])

    login_user(newuser)  # login the user
    flash('Account Created!')  # send message
    return redirect('layout.html')  # redirect to homepage

  except Exception:  # attempted to insert a duplicate user
    rollback()
    flash("username or email already exists")  # error message
    return redirect(url_for('login_page'))

@user_views.route('/logout', methods=['GET'])
@login_required
def logout_action():
  logout_user_action()
  flash('Logged Out')
  return redirect('/')

@user_views.route('/userjson', methods=['GET'])
def get_exerciseData_page():
    users = get_all_users_json()
    return jsonify(users)