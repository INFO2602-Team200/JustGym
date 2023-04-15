from App.database import db
from App.models import Workout
from .exercise import(get_exercises_by_workoutID)


def get_workout (workout_id):
    workout = Workout.query.filter_by(workout_id =workout_id).first()
    if workout:
        return workout
    return None

def add_workout(user_id,workoutName):
    new_workout = Workout(user_id = user_id, workoutName = workoutName)

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





