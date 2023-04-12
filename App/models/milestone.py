from App.database import db

class Milestone(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user_data.user_id'), primary_key = True)
    dateObtained = db.Column(db.Date, nullable = False)


def __init__(self, user_id, dateObtained):
    self.user_id = user_id
    self.dateObtained = dateObtained