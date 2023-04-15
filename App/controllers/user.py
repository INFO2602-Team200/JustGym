from App.models import User
from App.database import db
import App.controllers.userData as user_data
import App.controllers.userPreferences as user_preferences

def create_user(username, password, email,dateOfBirth,height,weight,sex, data = [], preferences = []):
    newuser = User(username=username, password=password,email = email,dateOfBirth = dateOfBirth,height = height,weight = weight,sex = sex, data = data,preferences = preferences)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user_by_email(email):
    return User.query.filter_by(email = email).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username, email,dateOfBirth,height,weight,sex):
    user = get_user(id)
    if user:
        user.username = username
        user.email = email
        user.dateOfBirth = dateOfBirth
        user.height = height
        user.weight = weight
        user.sex = sex
        db.session.add(user)
        return db.session.commit()
    return None

def rollback():
    db.session.rollback()

# Function creates User Data and User Preferences for a User
def add_user_information(user_id, darkMode, height_units, weight_units):
    user = get_user(user_id)
    new_user_data = user_data.addUserData(user_id)
    new_user_preferences = user_preferences.addUserPreferences(user_id,darkMode,height_units,weight_units)
    
    if new_user_data:
        user.data = new_user_data
        if new_user_preferences:
            user.preferences = new_user_preferences
            db.session.add(user)
            db.session.commit()
            return True
    return None
