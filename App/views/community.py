from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, json,url_for,flash
from App.models import db
from App.controllers import get_community,copy_Workout,get_community_workout, get_all_exercises,get_exercises_by_workoutID,addVote,addDownVote, get_community_workout_by_communityWorkoutId
from.index import index_views
from flask_login import login_required,current_user


community_views = Blueprint('community_views', __name__, template_folder='../templates')

@community_views.route('/community/<int:communityWorkoutId>', methods=['GET'])
@login_required
def community_workout_page(communityWorkoutId):
    # community = get_community(1) # there is only 1 active community
    community_workout  = get_community_workout_by_communityWorkoutId(communityWorkoutId)
    
    if community_workout:
        workout = community_workout.workout
        exercises = get_exercises_by_workoutID(workout.workout_id)

        from App.controllers import seconds_to_minutes_string, get_num_exercises_workout
        seconds = workout.estimatedDuration
        workoutDuration = seconds_to_minutes_string(seconds)
        numExercises = get_num_exercises_workout(workout.workout_id)

    else:
        from App.controllers import seconds_to_minutes_string
        exercises = []
        workoutDuration = seconds_to_minutes_string(0)
        numExercises = 0


    return render_template('community_workout.html',community_workout = community_workout,  exercises = exercises, workoutDuration = workoutDuration, numExercises = numExercises)


@community_views.route('/communitycopy/<int:communityWorkoutId>', methods=['GET'])
@login_required
def add_community_workout(communityWorkoutId):
    community_workout  = get_community_workout_by_communityWorkoutId(communityWorkoutId)

    if community_workout:
        status = copy_Workout(community_workout.workoutId)

        if status:
            flash('Community workout Added successfully!')
        else:
            flash('Error: Community workout failed to be added!') 
        return redirect(request.referrer)


@community_views.route('/voteup/<int:communityWorkoutId>', methods=['GET'])
@login_required
def vote_up(communityWorkoutId):
    status = addVote(communityWorkoutId)

    if status:
        flash("Added Vote")
    else: 
        flash("Vote Unsucessful")
    return redirect(request.referrer)

@community_views.route('/votedown/<int:communityWorkoutId>', methods=['GET'])
@login_required
def vote_down(communityWorkoutId):
    status = addDownVote(communityWorkoutId)

    if status:
        flash("Added Vote")
    else: 
        flash("Vote Unsucessful")
    return redirect(request.referrer)


@community_views.route('/comm', methods=['GET'])
@login_required
def test_page_community():
    
    return render_template('community_workout.html')