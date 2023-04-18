from App.database import db

class Community(db.Model):
    communityId = db.Column(db.Integer, primary_key = True)
    communityWorkout= db.relationship('communityWorkout',backref = 'community', lazy = True)


    def __init__(self, communityWorkout):
        self.communityWorkout = communityWorkout 
        

    def get_json(self):
        return{
        'communityWorkout': self.communityWorkout,
        'communityId': self.communityId
        }