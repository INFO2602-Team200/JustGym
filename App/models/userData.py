from App.database import db

class UserData(db.Model):
    __tablename__ = 'user_data'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    myWorkouts = db.relationship('Workout', backref='userdata', lazy='dynamic')
    myCommunityWorkouts = db.Column(db.String)
    myMilestones = db.relationship('Milestone', backref='userdata', lazy='dynamic')
    myEquipment = db.Column(db.String)

    def __init__(self,user_id,myWorkouts,myMilestones,myEquipment, myCommunityWorkouts):
        self.user_id = user_id
        self.myWorkouts = myWorkouts
        self.myCommunityWorkouts = myCommunityWorkouts
        self.myMilestones = myMilestones
        self.myEquipment = myEquipment

    def get_json(self):
        from App.controllers import get_user_workouts_json, get_user_milestones_json,get_user_community_workouts_json


        return{
            'user_id': self.user_id,
            'myWorkouts': get_user_workouts_json(self.user_id),
            'myMilestones': get_user_milestones_json(self.user_id),
            'myCommunityWorkouts' : get_user_community_workouts_json(self.user_id),
            'myEquipment': self.myEquipment
        }
    
