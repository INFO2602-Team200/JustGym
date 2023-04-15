from App.database import db

class UserPreferences(db.Model):
    __tablename__ = "user_preferences"

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    darkMode = db.Column(db.Boolean, nullable = False, default = False)
    height_units = db.Column(db.String, nullable = False, default = "Metres")
    weight_units = db.Column(db.String, nullable = False, default = "Kilograms")
    
    def __init__(self, user_id, dark_mode,height_units, weight_units):
        self.user_id = user_id
        self.dark_mode = dark_mode
        self.height_units = height_units
        self.weight_units = weight_units

    def get_json(self):
        return {
            # 'user_id': self.user_id,
            'darkMode': self.darkMode,
            'height_units': self.height_units,
            'weight_units': self.weight_units
        }