from App.database import db
from App.models import UserData

def addUserData(user_id, my_workouts=[], my_milestones=[]):
    new_user_data = UserData(user_id=user_id, myWorkouts=my_workouts, myMilestones=my_milestones)
    db.session.add(new_user_data)
    db.session.commit()

def removeUserData(user_id):
    terminated_userData = UserData.query.filter_by(user_id = user_id).first()
    if terminated_userData:
        db.session.delete(terminated_userData)
        db.session.commit()
        return True
    return False

def get_userData(user_id):        
        data = UserData.query.filter_by(user_id = user_id).first()
        if data:
            return data
        return None

def get_userData_json(user_id):        
    data = get_userData(user_id)
    if data:
            return data.get_json()
    return None
