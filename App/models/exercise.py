from App.database import db
from App.controllers import (get_exerciseData,get_exerciseData_json)

class Exercise(db.Model):

    __tablename__ = 'exercise'

    exerciseID = db.Column(db.Integer, primary_key = True)
    workoutId = db.Column(db.Integer,db.ForeignKey('workout.workout_id'))
    exerciseDataId = db.Column(db.Integer, db.ForeignKey('exercise_data.id'))
    exercise = db.relationship('ExerciseData', backref='exercise',lazy = True)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    duration = db.Column(db.Integer)


    def __init__(self,workoutId,exerciseDataId,sets, reps, duration):
        self.workoutId = workoutId
        self.exerciseDataId = exerciseDataId
        self.exercise = get_exerciseData(exerciseDataId)
        self.sets = sets
        self.reps = reps
        self.duration = duration

    def get_json(self):
        return {
            'exerciseID': self.exerciseID,
            'workoutId': self.workoutId,
            'exerciseDataId': self.exerciseDataId,
            'exerciseData': self.get_exerciseData_json(self.exerciseDataId),
            'sets': self.sets,
            'reps': self.reps,
            'duration': self.duration
        }