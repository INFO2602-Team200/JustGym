from App.database import db

class Workout(db.Model):
    workout_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_data.user_id'), nullable = False)
    workoutName = db.Column(db.String(120), nullable=False)
    workoutExercises = db.relationship('Exercise', backref='workout', lazy=True)
    estimatedDuration = db.Column(db.Integer ,default = 0)

    def __init__(self, user_id, workoutName,workoutExercises, estimatedDuration):
        self.user_id = user_id
        self.workoutName = workoutName
        self.workoutExercises = workoutExercises
        self.estimatedDuration = estimatedDuration

    def get_json(self):
        return{
            'workout_id': self.workout_id,
            'workoutName': self.workoutName,
            'workoutExercises': self.workoutExercises,
            'estimatedDuration': self.estimatedDuration


        }