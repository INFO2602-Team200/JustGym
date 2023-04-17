from App.database import db

class communityWorkout (db.Model):
    communityWorkoutId = db.Column(db.Integer, primary_key = True)
    communityId = db.Column(db.Integer,  db.ForeignKey('community.communityId'))
    workoutId = db.Column(db.Integer,db.ForeignKey('workout.workout_id')) 
    workout = db.relationship('Workout',backref = 'communityWorkout', lazy = True)
    upvotes = db.Column(db.Integer, default = 0)
    downvotes = db.Column(db.Integer, default = 0)
    netvotes = db.Column(db.Integer, default = 0)

    def __init__(self,communityId, workoutId,workout,upvotes,downvotes):
        self.communityId = communityId
        self.workout = workout
        self.workoutId = workoutId
        self.upvotes = upvotes
        self.downvotes = downvotes
        

    def get_json(self):
        return{
        'communityWorkoutId': self.communityWorkoutId,
        'communityId': self.communityId,
        'workout': self.workout,
        'upvotes': self.upvotes,
        'downvotes': self.downvotes,
        'netvotes': self.netvotes
        }
    