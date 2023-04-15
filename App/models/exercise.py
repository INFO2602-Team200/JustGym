from App.database import db


class Exercise(db.Model):

    __tablename__ = 'exercise'

    exerciseID = db.Column(db.Integer, primary_key = True)
    workoutId = db.Column(db.Integer,db.ForeignKey('workout.workout_id'))
    exerciseDataId = db.Column(db.Integer, db.ForeignKey('exercise_data.id'))
    exercise = db.relationship('ExerciseData', backref='exercise',lazy = True)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    duration = db.Column(db.Integer)


    def __init__(self,workoutId,exerciseDataId,sets, reps, duration, exercise):
        self.workoutId = workoutId
        self.exerciseDataId = exerciseDataId
        self.sets = sets
        self.reps = reps
        self.duration = duration
        self.exercise = exercise

    def get_json(self):
        from App.controllers import (get_exerciseData_json)
        return {

            'exerciseID': self.exerciseID,
            # 'workoutId': self.workoutId,
            # 'exerciseDataId': self.exerciseDataId,
            'exercise': get_exerciseData_json(self.exerciseDataId),
            'sets': self.sets,
            'reps': self.reps,
            'duration': self.duration
        }