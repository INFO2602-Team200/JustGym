from App.database import db

class Exercise(db.Model):

    __tablename__ = 'exercise'

    exerciseID = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('workout.workout_id'))
    exerciseDataId = db.Column(db.Integer, db.ForeignKey('exercise_data.id'))
    exercise = db.relationship('ExerciseData', backref='exercise')
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    duration = db.Column(db.Integer)


def __init__(self,sets, reps, duration):
    self.exercise = []
    self.sets = sets
    self.reps = reps
    self.duration = duration