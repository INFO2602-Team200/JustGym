from App.database import db


class Milestone(db.Model):
    milestoneId = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_data.user_id'))
    milestoneDataId = db.Column(db.Integer,db.ForeignKey("milestone_data.milestoneDataId"))
    milestone = db.relationship('MilestoneData', backref='milestone')
    dateObtained = db.Column(db.Date, nullable = False)


    def __init__(self, user_id,milestoneDataId, milestone,dateObtained):
        self.user_id = user_id
        self.dateObtained = dateObtained
        self.milestone = milestone
        self.milestoneDataId = milestoneDataId

    def get_json(self):
        from App.controllers import get_milestoneData_json
        return {
            
            'milestoneId': self.milestoneId,
            'user_id': self.user_id,
            'milestoneDataId': self.milestoneDataId,
            'milestone': get_milestoneData_json(self.milestoneDataId),
            'dateObtained': self.dateObtained
        }
