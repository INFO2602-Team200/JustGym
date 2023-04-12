from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120),nullable = False, unique = True)
    age = db.Column(db.String(120), nullable = False)
    height = db.Column(db.Float, nullable = False)
    weight = db.Column(db.Float, nullable = False)
    sex = db.Column(db.String(120), nullable = False)
    data = db.relationship('UserData', backref= db.backref('user'), lazy = 'joined')
    preferences = db.relationship('UserPreferences', backref= db.backref('user'), lazy = 'joined')

    def __init__(self, username, password,email,age,height,weight,sex,data = None ,preferences = None):
        self.username = username
        self.email = email
        self.age = age
        self.height = height
        self.weight = weight
        self.sex = sex
        self.data = data
        self.preferences = preferences
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'email' : self.email,
            'age' : self.age,
            'height': self.height,
            'weight': self.weight,
            'sex' : self.sex,
            'data' : self.data,
            'preferences' : self.preferences,
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

