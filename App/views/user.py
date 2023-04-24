from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user
from App.models import User
from datetime import date
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
    extract_date_components,
    add_user_information,
    get_userEquipment,
    get_user,
    get_all_exercise_equipment,
    check_milestones,
    get_user_milestones,
    update_user,
    add_user_equipment
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

# API Endpoints
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
@login_required
def identify_user_action():
    return jsonify({'message': f"username: {current_user.username}, id : {current_user.id}"})


# View Routes
@user_views.route('/signup', methods=['GET'])
def signup_page():
  return render_template('signup.html')


@user_views.route('/login', methods=['GET'])
def login_page():
  return render_template('login.html')

# Action routes

@user_views.route('/login', methods=['POST'])
def login_action():
  data = request.form
  user = User.query.filter_by(username=data['username']).first()
  if user and user.check_password(data['password']):  # check credentials
    flash('Logged in successfully.')  # send message to next page
    login_user(user,True)  # login the user
    return redirect('/home')  # redirect to main page if login successful
  else:
    flash('Invalid username or password')  # send message to next page
  return redirect('/')


@user_views.route('/signup', methods=['POST'])
def signup_action():
  try:
    data = request.form  # get data from form submission
    year,month,day = extract_date_components(data['dateOfBirth'])
    dob = date(year,month,day)

    newuser =create_user(username=data['username'], email=data['email'], password=data['password'], dateOfBirth = dob , height = data['height'],weight = data['weight'],sex = data['sex'])
    status = add_user_information(newuser.id,True,"Centimetres","Kilograms")
    login_user(newuser,False)  # login the user
    flash('Account Created!')  # send message
    return redirect("/equipment")  # redirect to homepage

  except Exception:  # attempted to insert a duplicate user
    rollback()
    flash("username or email already exists")  # error message
    return redirect(url_for('user_views.login_page'))

@user_views.route('/logout', methods=['GET'])
@login_required
def logout_action():
  logout_user_action()
  flash('Logged Out')
  return redirect('/')


@user_views.route('/profile', methods=['GET'])
@login_required
def profile():
    user = get_user(current_user.id)
    userEquipment = get_userEquipment(current_user.id)
    equipment = get_all_exercise_equipment()

    check_milestones(current_user.id)

    milestones = get_user_milestones(current_user.id)

    return render_template('profile.html', user=user, userEquipment=userEquipment, equipment=equipment, milestones=milestones)


@user_views.route('/profile', methods=['POST']) 
@login_required
def update_profile():
    formData = request.form
    equipment = request.form.getlist('equipment')
    
    user = get_user(current_user.id)

    update_user(current_user.id, formData['username'], 
                formData['email'], formData['dateOfBirth'], 
                formData['height'], formData['weight'], formData['sex'])

    add_user_equipment(current_user.id, equipment)

    return redirect(request.referrer)