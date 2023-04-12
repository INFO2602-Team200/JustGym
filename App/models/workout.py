from App.database import db

class Workout(db.Model):
    workout_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_data.user_id'), nullable = False)
    workoutName = db.Column(db.String(120), nullable=False)
    workoutExercises = db.relationship('Exercise', backref='workout', lazy='dynamic')
    estimatedDuration = db.Column(db.Integer)

    def __init__(self, user_id, workoutName, estimatedDuration):
        self.user_id = user_id
        self.workoutName = workoutName
        self.workoutExercises = []
        self.estimatedDuration = estimatedDuration