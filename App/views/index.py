from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json
from App.models import db
from App.controllers import create_user,add_user_information
from App.controllers import (add_exerciseData, add_exercise, 
                             add_workout,add_workout_exercise,
                             add_community,workout_public_status, 
                             add_user_equipment, 
                             load_milestone_data,
                             check_milestones,load_categories)
                    
from datetime import date
from flask_login import LoginManager, current_user, login_user, login_required, logout_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('login.html')



# Categories-exercises modal action route 

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

    
    load_categories()

    workout_test = add_workout(1,"Full Body Workout",False,"1")
    workout_test = add_workout(1,"Legs Workout",False,"2")
    
    workout_test = add_workout_exercise(2,add_exercise(2,1,4,5,60))
    workout_test = add_workout_exercise(1,add_exercise(1,14,4,5,30))
    workout_test = add_workout_exercise(2,add_exercise(2,23,4,5,15))

    
    workout_test = add_workout_exercise(1, add_exercise(1,1,4,5,45))

    workout_test = add_workout(2,"Chest Workout",True,"3")
    workout_test3 = add_workout_exercise(3, add_exercise(3,9,4,5,85))

    workout_test = add_workout(2,"Abs Workout",False,"4")
    workout_test = add_workout_exercise(4, add_exercise(4,8,4,5,45))

    new_community = add_community()

    status = workout_public_status(workout_test3.workout_id)
    
    eq = ['cable', 'leverage machine', 'band','tire']
    stat = add_user_equipment(1,eq)

    load_milestone_data()
 
    check_milestones(1)
    check_milestones(2)

    # Close the session
    db.session.commit()

    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})
  
