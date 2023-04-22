from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from App.models import db
from App.controllers import get_user_workouts, get_all_categories,add_workout, get_workout
from flask_login import LoginManager, current_user, login_user, login_required, logout_user



workout_views = Blueprint('workout_views', __name__, template_folder='../templates')

@workout_views.route('/home', methods=['GET'])
@login_required
def home_page():
    categories = get_all_categories()
    myWorkouts = get_user_workouts(current_user.id)

    return render_template('home.html',categories = categories, myWorkouts = myWorkouts)

@workout_views.route('/home/<int:workoutID>', methods=['GET'])
@login_required
def view_workout(workoutID):
    workout = get_workout(workoutID)

    return render_template('workout_exercises.html', workout=workout, workoutID=workoutID)

@workout_views.route('/home/<int:workoutID>', methods=['POST'])
@login_required
def update_workout(workoutID):
    formData = request.form

    # TODO : update exercise data & send workout id through form

    return redirect(request.referrer)

# Route used to add a new workout Routine
@workout_views.route('/workout', methods=['POST'])
@login_required
def add_new_workout():
    formData = request.form
    add_workout(current_user.id,formData['workoutName'], formData['public'], formData['categoryId'])

    return redirect(request.referrer)