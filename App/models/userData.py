from App.database import db

class UserData(db.Model):
    __tablename__ = 'user_data'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    myWorkouts = db.relationship('Workout', backref='userdata', lazy='dynamic')
    myMilestones = db.relationship('Milestone', backref='userdata', lazy='dynamic')

    def __init__(self,user_id,myWorkouts,myMilestones):
        self.user_id = user_id
        self.myWorkouts = myWorkouts
        self.myMilestones = myMilestones

    def get_json(self):
        from App.controllers import get_user_workouts_json


        return{
            # 'user_id': self.user_id,
            'myWorkouts': get_user_workouts_json(self.user_id),
            # 'myMilestones': self.myMilestones
        }
    
