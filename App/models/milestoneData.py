from App.database import db


class MilestoneData(db.Model):
    milestoneDataId = db.Column(db.Integer, primary_key = True)
    milestoneName = db.Column(db.String, nullable = False)
    condition = db.Column(db.String)


    def __init__(self, milestoneName,condition):
        self.milestoneName = milestoneName
        self.condition = condition

    def get_json(self):
        return{
            'milestoneDataId': self.milestoneDataId,
            'milestoneName': self.milestoneName,
            'condition': self.condition

        }


