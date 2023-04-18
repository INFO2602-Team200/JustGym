from App.database import db

class Workout(db.Model):
    workout_id = db.Column(db.Integer, primary_key = True )
    user_id = db.Column(db.Integer, db.ForeignKey('user_data.user_id'), nullable = False)
    workoutName = db.Column(db.String(120), nullable=False)
    workoutExercises = db.relationship('Exercise', backref='workout', lazy=True)
    estimatedDuration = db.Column(db.Integer ,default = 0)
    public = db.Column(db.Boolean ,default = False)
    category = db.Column(db.String, default = False)

    def __init__(self, user_id, workoutName,workoutExercises, estimatedDuration,public,category):
        self.user_id = user_id
        self.workoutName = workoutName
        self.workoutExercises = workoutExercises
        self.estimatedDuration = estimatedDuration
        self.public = public
        self.category = category

    def get_json(self):

        from App.controllers import get_exercises_by_workoutID_json
        return{
            'workout_id': self.workout_id,
            'workoutName': self.workoutName,
            'workoutExercises': get_exercises_by_workoutID_json(self.workout_id),
            'estimatedDuration': self.estimatedDuration,
            'public': self.public,
            'category': self.category
        }