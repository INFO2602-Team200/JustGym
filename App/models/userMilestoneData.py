from App.database import db


class UserMilestoneData(db.Model):

    __tablename__ = 'user_milestone_data'

    milestoneId = db.Column(db.Integer,db.ForeignKey("milestone_data.milestoneId") ,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey("milestone.user_id"), primary_key = True)
   

def __init__(self, user_id, milestoneId):
    self.user_id = user_id
    self.milestoneId = milestoneId
