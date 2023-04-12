from App.models import User, UserData, UserPreferences
from App.database import db

def create_user(username, password, email,age,height,weight,sex):
    newuser = User(username=username, password=password,email = email,age = age,height = height,weight = weight,sex = sex)
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

def update_user(id, username, email,age,height,weight,sex):
    user = get_user(id)
    if user:
        user.username = username
        user.email = email
        user.age = age
        user.height = height
        user.weight = weight
        user.sex = sex
        db.session.add(user)
        return db.session.commit()
    return None
    