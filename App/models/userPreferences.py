from App.database import db

class UserPreferences(db.Model):
    __tablename__ = "user_preferences"

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    darkMode = db.Column(db.Boolean, nullable = False, default = False)

    def __init__(self, dark_mode=False):
        self.dark_mode = dark_mode