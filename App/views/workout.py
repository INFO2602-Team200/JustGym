from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from App.models import db
from App.controllers import get_user_workouts, get_all_categories,add_workout,get_community, render_community_workouts, get_workout,get_exercises_by_workoutID,delete_exercise,get_all_category_exercises,seconds_to_minutes_string,modify_exercise,get_userData,modify_workout,get_num_exercises_workout
from flask_login import LoginManager, current_user, login_user, login_required, logout_user



workout_views = Blueprint('workout_views', __name__, template_folder='../templates')

@workout_views.route('/home', methods=['GET'])
@login_required
def home_page():
    categories = get_all_categories()
    myWorkouts = get_user_workouts(current_user.id)
    data = get_userData(current_user.id)
    community = get_community(1)
    community_workouts = community.communityWorkout

    # communityWorkoutIds = data.myCommunityWorkouts
    # myCommunityWorkouts = render_community_workouts(communityWorkoutIds)
    return render_template('home.html',categories = categories, myWorkouts = myWorkouts, community_workouts = community_workouts)




@workout_views.route('/home/<int:workoutID>', methods=['GET'])
@login_required
def view_workout(workoutID):
    workout = get_workout(workoutID)
    exercises = get_exercises_by_workoutID(workoutID)
    category_exercises = get_all_category_exercises(workout.category.categoryName)

    workout = get_workout(workoutID)
    seconds = workout.estimatedDuration
    workoutDuration = seconds_to_minutes_string(seconds)
    numExercises = get_num_exercises_workout(workoutID)



    return render_template('exercise_routine.html',workout = workout, category_exercises =category_exercises , exercises = exercises, workoutID=workoutID,workoutDuration = workoutDuration,numExercises = numExercises)




@workout_views.route('/home/<int:workoutID>/<int:exerciseId>', methods=['POST'])
@login_required
def update_workout(workoutID,exerciseId):
    formData = request.form

    modified_exercise= modify_exercise(exerciseId,formData['exerciseDataId'],formData['sets'],formData['reps'],formData['duration'])
    if modified_exercise:
        flash('Exercise successfully modified!')
    else:
        flash('Error: Unable to modify exercise!')
        
    return redirect(request.referrer)




@workout_views.route('/home/<int:workoutID>/<int:exerciseId>', methods=['GET'])
@login_required
def delete_workout_exercise(workoutID,exerciseId):
    status = delete_exercise(exerciseId)
    
    if status == False:
        flash('Invalid id or unauthorized')
    else:
        flash('Exercise Deleted!')

    return redirect(request.referrer)




@workout_views.route('/home/<int:workoutID>', methods=['GET'])
@login_required
def rename_workout(workoutID):
    formData = request.form
    modified_workout = modify_workout(workoutID, formData['workoutName'])
    if modified_workout:
        flash('Workout Name successfully changed!')
    else:
        flash('Unable to change Workout Name.')
    return redirect(request.referrer)



# Route used to add a new workout Routine
@workout_views.route('/workout', methods=['POST'])
@login_required
def add_new_workout():
    formData = request.form
    add_workout(current_user.id,formData['workoutName'], formData['public'], formData['categoryId'])

    return redirect(request.referrer)

