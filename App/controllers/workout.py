from App.database import db
from App.models import Workout
from .exercise import(workoutEstimation)
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

def add_workout(user_id,workoutName,public,category, workoutExercises = [], estimatedDuration = 0):
    new_workout = Workout(user_id = user_id, workoutName = workoutName, workoutExercises= workoutExercises, estimatedDuration = estimatedDuration, public = public, category = category)
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

def add_workout_exercise(workout_id, exercise):
    workout = get_workout(workout_id)
    if workout:
        workout.workoutExercises.append(exercise)
        workout.estimatedDuration = workoutEstimation(workout_id)
        db.session.add(workout)
        db.session.commit()
        return workout
    return None

def workout_public_status(workoutId):
    from App.controllers import create_community_workout,remove_community_workout,add_community_workout,delete_community_workout

    workout = get_workout(workoutId)
    if workout.public == False:
        status1 = delete_community_workout(workoutId)
        status2 = remove_community_workout(workoutId)
        return status1 and status2

    elif workout.public == True:
        community_workout = create_community_workout(workoutId)
        if community_workout:
            status = add_community_workout(1,community_workout)
            return status
            
    return False

def toggle_public_status(workoutId):
    workout = get_workout(workoutId)

    if workout:
        if workout.public == False:
                workout.public = True
                db.session.add()
                db.session.commit()
                status = workout_public_status(workoutId)


        elif workout.public == True:
                workout.public = False        
                db.session.add()
                db.session.commit()
                status = workout_public_status(workoutId)

        if not status:
            db.session.rollback()
        
        return workout.public
    
    return False

