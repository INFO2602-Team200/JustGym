from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json
from App.models import db
from App.controllers import create_user,add_user_information
from App.controllers import (add_exerciseData, add_exercise, 
                             add_workout,add_workout_exercise,
                             add_community,workout_public_status)
from datetime import date

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('login.html')

@index_views.route('/home', methods=['GET'])
def home_page():
    return render_template('home.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    bob = create_user('bob', 'bobpass',"bob@mail.com",date(1990, 5, 12) ,169,121,"Male")
    rob = create_user('rob', 'robpass',"rob@mail.com",date(1999, 5, 12),140, 90 ,"Male")
    add_user_information(bob.id,True,"Metres","Kilograms")
    add_user_information(rob.id,False,"Feet","Pounds")


    
    with open('App\exercises.json', 'r') as f:
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
    


    # Close the session
    db.session.commit()

    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})
  
 
#Routes for categories page, home page files to test functionality
@app.route('/categories', methods=['GET'])
def categories():
    return render_template('categories_page.html')


@app.route('/settings', methods=['GET'])
def settings():
    return render_template('settings.html')

@app.route('/logout', methods=['GET'])
def logout():
    return render_template('settings.html')


@app.route('/test', methods = ['GET'])
def test():
    file = open('App/exercises.json')
    data = json.load(file)

    return render_template('test_home.html', data = data)


@app.route('/test1', methods = ['GET'])
def test1():
    file = open('App/exercises.json')
    data = json.load(file)

    return render_template('test_exercises.html', data = data)
