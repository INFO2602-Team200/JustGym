from App.database import db
from App.models import UserData

def addUserData(user_id, my_workouts=[], my_milestones=[], my_equipment = []):
    new_user_data = UserData(user_id=user_id, myWorkouts=my_workouts, myMilestones=my_milestones,myEquipment=my_equipment)
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

def get_userEquipment(user_id):
     data = get_userData(user_id)
     print(data.myEquipment)
     if data:
          return data.myEquipment
     
def add_user_equipment(user_id,equipment):
    data = get_userData(user_id)
    if data:
        data.myEquipment = equipment
        db.session.add(data)
        db.session.commit()
        return True
    return False


# Milestone Functions
# accepts user_id and milestone object and appends milestone to myMilestones array in UserData
def append_user_milestone(user_id,milestone):
    user_data = get_userData(user_id)

    if user_data:
        user_data.myMilestones.append(milestone)
        db.session.add(user_data)
        db.session.commit()
        return True
    return False

def get_user_milestones(user_id):
    data = get_userData(user_id)
    if data:
         return data.myMilestones
    return []

def get_user_milestones_json(user_id):
    data = get_userData(user_id)
    if data:
         milestones = data.myMilestones
         return [milestone.get_json() for milestone in milestones]
    return []  
     
def check_user_milestone(user_id, milestoneDataId):
    user_milestones = get_user_milestones(user_id)
    
    for milestone in user_milestones:
         if milestone.milestoneDataId == milestoneDataId:
              return False
    return True
        