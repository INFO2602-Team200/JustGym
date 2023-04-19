from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from datetime import date
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120),nullable = False, unique = True)
    dateOfBirth = db.Column(db.Date, nullable = False)
    age = db.Column(db.String(120), nullable = False)
    height = db.Column(db.Float, nullable = False)
    weight = db.Column(db.Float , nullable = False)
    bmi = db.Column(db.Float ,nullable = False)
    sex = db.Column(db.String(120), nullable = False)
    data = db.relationship('UserData', backref= db.backref('user'), lazy = 'joined')
    preferences = db.relationship('UserPreferences', backref= db.backref('user'), lazy = 'joined')

    def __init__(self, username, password,email,dateOfBirth,height,weight,sex, data, preferences):
        self.username = username
        self.email = email
        self.dateOfBirth = dateOfBirth
        self.age = User.calculate_age(dateOfBirth)
        self.height = float(height)
        self.weight = float(weight)
        self.bmi = User.get_bmi(float(height),float(weight))
        self.sex = sex
        self.set_password(password)
        self.data = data
        self.preferences = preferences

    def get_json(self):
        from App.controllers import get_user_preference_json, get_userData_json

        return{
            'id': self.id,
            'username': self.username,
            'email' : self.email,
            'dateOfBirth': self.dateOfBirth,
            'age' : self.age,
            'height': self.height,
            'weight': self.weight,
            'bmi' : self.bmi,
            'sex' : self.sex,
            'data' : get_userData_json(self.id),
            'preferences' : get_user_preference_json(self.id),
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def calculate_age(dateOfBirth):
        today = date.today()
        age = today.year - dateOfBirth.year - ((today.month, today.day) < (dateOfBirth.month, dateOfBirth.day))
        return age

    # height - cm ,weight - kg
    def get_bmi(height, weight):
        bmi = float(weight/((height/100)*(height/100)*1.0))
        return round(bmi, 2)
