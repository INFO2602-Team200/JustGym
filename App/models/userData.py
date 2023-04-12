from App.database import db

class UserData(db.Model):
    __tablename__ = 'user_data'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    # myWorkouts = db.relationship('Workout', backref='userdata', lazy='dynamic')
    # myMilestones = db.relationship('Milestone', backref='userdata', lazy='dynamic')

def __init__(self):
    user_id = self.id
    # self.myWorkouts = []
    # self.myMilestones = []
