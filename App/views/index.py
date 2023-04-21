from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json
from App.models import db
from App.controllers import create_user,add_user_information
from App.controllers import (add_exerciseData, add_exercise, 
                             add_workout,add_workout_exercise,
                             add_community,workout_public_status,
                             get_all_exercises, get_user_workouts, 
                             get_user_workouts_json, get_workout_json,
                             get_user, get_userEquipment, getUserPreference,
                             update_user, get_all_exercise_equipment, add_user_equipment, add_milestone_data, add_user_milestone, append_user_milestone
                             ,check_milestones)
                             
from datetime import date
from flask_login import LoginManager, current_user, login_user, login_required, logout_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('login.html')

@index_views.route('/home', methods=['GET'])
def home_page():
    return render_template('test_home.html')


# Categories-exercises modal action route 
@index_views.route('/categories/<string:category>', methods=['POST'])
@index_views.route('/categories/<string:category>/<int:id>', methods=['POST'])
@login_required
def add_exercise_to_workout(category, id=1):
    formData = request.form

    exercise = add_exercise(formData['workout_id'], formData['selected_exercise_id'], formData['sets'], formData['reps'], formData['duration']) 
    add_workout_exercise(formData['workout_id'], exercise)
    
    return redirect(request.referrer)

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    bob = create_user('bob', 'bobpass',"bob@mail.com",date(1990, 5, 12) ,169,121,"Male")
    rob = create_user('rob', 'robpass',"rob@mail.com",date(1999, 5, 12),140, 90 ,"Male")
    add_user_information(bob.id,True,"Centimetres","Kilograms")
    add_user_information(rob.id,False,"Inches","Pounds")


    
    with open('App/exercises.json', 'r') as f:
        data = json.load(f)

    # Insert the data into the database
    for exercise in data:
        db_exercise = add_exerciseData(exercise)

    
    workout_test = add_workout(1,"Full Body Workout",False,"Full Body Workout")
    workout_test = add_workout(1,"Legs Workout",False,"Legs Workout")
    
    workout_test = add_workout_exercise(2,add_exercise(2,1,4,5,60))
    workout_test = add_workout_exercise(1,add_exercise(1,14,4,5,30))
    workout_test = add_workout_exercise(2,add_exercise(2,23,4,5,15))

    
    workout_test = add_workout_exercise(1, add_exercise(1,1,4,5,45))

    workout_test = add_workout(2,"Back Workout",True,"Body Workout")
    workout_test3 = add_workout_exercise(3, add_exercise(3,9,4,5,85))

    workout_test = add_workout(2,"Abs Workout",False,"Abs Workout")
    workout_test = add_workout_exercise(4, add_exercise(4,8,4,5,45))

    new_community = add_community()

    status = workout_public_status(workout_test3.workout_id)
    
    eq = ['cable', 'leverage machine', 'band','tire']
    stat = add_user_equipment(1,eq)


    # Milestone Tests
    add_milestone_data("Fresh Meat","Awarded for creating a JustGym account")
    add_milestone_data("Getting Started","Created your first Workout")
    add_milestone_data("1+1 = 2","Created your second Workout")
    add_milestone_data("Let's get pumpin'","Added your first exercise")

    # m_stone = add_user_milestone(1,1)
    # append_user_milestone(1,m_stone)
    check_milestones(1)
    check_milestones(2)

    # Close the session
    db.session.commit()

    
    # test = get_all_exercises()
    # print("test")
    # print(test)

    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})
  
 
#Routes for categories page, home page files to test functionality
@index_views.route('/categories', methods=['GET'])
@login_required
def categories():
    return render_template('categories_page.html')


@index_views.route('/settings', methods=['GET'])
@login_required
def settings():
    return render_template('settings.html')

@index_views.route('/test', methods = ['GET'])
@login_required
def test():
    file = open('App/exercises.json')
    data = json.load(file)

    return render_template('test_home.html', data = data)


@index_views.route('/test1', methods = ['GET'])
@login_required
def test1():
    file = open('App/exercises.json')
    data = json.load(file)

    return render_template('test_exercises.html', data = data)

@index_views.route('/profile', methods=['GET'])
@login_required
def profile():
    user = get_user(current_user.id)
    userEquipment = get_userEquipment(current_user.id)
    equipment = get_all_exercise_equipment()
    preferences = getUserPreference(current_user.id)

    check_milestones(current_user.id)

    height_units = preferences.height_units
    weight_units = preferences.weight_units

    return render_template('profile.html', user=user, userEquipment=userEquipment,height_units=height_units, weight_units=weight_units,equipment = equipment)

@index_views.route('/profile', methods=['POST']) 
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