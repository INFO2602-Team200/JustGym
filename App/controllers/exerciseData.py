from App.database import db
from App.models import ExerciseData

def add_exerciseData(exercise):
    db_exercise = ExerciseData(id=exercise['id'], name=exercise['name'], bodyPart=exercise['bodyPart'], equipment=exercise['equipment'], target=exercise['target'], gifUrl=exercise['gifUrl'])
    db.session.add(db_exercise)
    
    return db_exercise
