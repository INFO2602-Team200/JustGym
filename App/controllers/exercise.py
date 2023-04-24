from App.database import db
import App.models.exercise as e
from App.controllers.exerciseData import (get_exerciseData)

def add_exercise(workoutId, exerciseDataId, sets, reps, duration):
    exercise= get_exerciseData(exerciseDataId)
    new_exercise = e.Exercise(workoutId=workoutId, exerciseDataId=exerciseDataId, sets=sets, reps=reps, duration=duration, exercise=exercise)
    db.session.add(new_exercise)
    db.session.commit()
    return new_exercise

def modify_exercise(exerciseId,exerciseDataId,sets,reps,duration):
    updated_exercise = get_exercise(exerciseId)

    if updated_exercise:
        updated_exercise.sets = sets
        updated_exercise.reps = reps
        updated_exercise.exerciseDataId = exerciseDataId
        updated_exercise.exercise = get_exerciseData(exerciseDataId)
        updated_exercise.duration = duration
        db.session.add(updated_exercise)
        db.session.commit()
        from App.controllers import get_workout
        updated_workout = get_workout(updated_exercise.workoutId)
        updated_workout.estimatedDuration = workoutEstimation(updated_exercise.workoutId)
        
        db.session.add(updated_workout)
        db.session.commit()
        
        return updated_exercise

    return None

def delete_exercise(exerciseId):
    terminated_exercise = get_exercise(exerciseId)
    
    if terminated_exercise:
        db.session.delete(terminated_exercise)

        from App.controllers import get_workout
        updated_workout = get_workout(terminated_exercise.workoutId)
        updated_workout.estimatedDuration = workoutEstimation(terminated_exercise.workoutId)
        
        db.session.add(updated_workout)
        db.session.commit()
        
        # db.session.commit()
        return True
    return False

def get_exercise(exerciseId):
    found_exercise =e.Exercise.query.filter_by(exerciseID = exerciseId).first()
    if found_exercise:
        return found_exercise
    return None

def get_exercises_by_workoutID(workoutID):
    workout_exercises = e.Exercise.query.filter_by(workoutId = workoutID)
    if workout_exercises:
        return workout_exercises
    return None

def get_exercises_by_workoutID_json(workoutID):
    workout_exercises = get_exercises_by_workoutID(workoutID)
    if workout_exercises:    
        return [workout_exercise.get_json() for workout_exercise in workout_exercises]
    return []

def workoutEstimation(workoutID):
    exercises = get_exercises_by_workoutID(workoutID)
    if exercises:
        estimatedDuration = 0
        for exercise in exercises:
            estimatedDuration = exercise.duration + estimatedDuration

        return estimatedDuration
    return 0

def get_num_exercises(user_id,workoutExercises):
    return len(workoutExercises)
        
def get_num_exercises_workout(workoutId):
    exercises = get_exercises_by_workoutID(workoutId)
    return exercises.count()