from App.database import db
from App.models import ExerciseData

def add_exerciseData(exercise):
    db_exercise = ExerciseData(id=exercise['id'], name=exercise['name'], bodyPart=exercise['bodyPart'], equipment=exercise['equipment'], target=exercise['target'], gifUrl=exercise['gifUrl'])
    db.session.add(db_exercise)
    return db_exercise

def get_all_exercises():
    return ExerciseData.query.all()

def get_all_exercises_json():
    exercises = get_all_exercises()
    if not exercises:
        return []
    exerciseList = [ exercise.get_json() for exercise in exercises]
    return exerciseList