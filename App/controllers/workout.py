from App.database import db
from App.models import Workout
from .exercise import(get_exercises_by_workoutID)


def get_workout (workout_id):
    workout = Workout.query.filter_by(workout_id =workout_id).first()
    if workout:
        return workout
    return None

def get_user_workouts (user_id):
    workouts = Workout.query.filter_by(user_id =user_id)
    if workouts:
        return workouts
    return None

def add_workout(user_id,workoutName, workoutExercises = [], estimatedDuration = 0):
    new_workout = Workout(user_id = user_id, workoutName = workoutName, workoutExercises= workoutExercises, estimatedDuration = estimatedDuration)
    if new_workout:
        db.session.add(new_workout)
        db.session.commit()
        return new_workout
    return None

def modify_workout(workout_id,workoutName):
    modified_workout = get_workout(workout_id)
    if modified_workout:
        modified_workout.workoutName = workoutName
        db.session.add(modified_workout)
        db.session.commit()
        return modified_workout
    
    return None

def delete_workout(workout_id):
    terminated_workout = get_workout(workout_id)
    if terminated_workout:
        db.session.delete(terminated_workout)
        db.session.commit()
        return True

    return False


def get_workout_json(workout_id):
    workout = get_workout(workout_id)
    if workout:
        return workout.get_json()
    return None        

def get_user_workouts_json(user_id):
    workouts = get_user_workouts(user_id)
    if workouts:
        return [workout.get_json() for workout in workouts]
    return None


