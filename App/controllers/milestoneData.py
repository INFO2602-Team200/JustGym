from App.database import db
from App.models import MilestoneData

def add_milestone_data(milestoneName,condition):
    new_milestoneData = MilestoneData(milestoneName = milestoneName,condition = condition)
    db.session.add(new_milestoneData)
    db.session.commit()

def get_milestoneData(milestoneDataId):
    milestoneData = MilestoneData.query.filter_by(milestoneDataId = milestoneDataId).first()
    if milestoneData:
        return milestoneData
    return None

def get_milestoneData_json(milestoneDataId):
    milestoneData = MilestoneData.query.filter_by(milestoneDataId = milestoneDataId).first()
    if milestoneData:
        return milestoneData.get_json()
    return None

def remove_milestone_data(milestoneDataId):
    milestoneData = get_milestoneData(milestoneDataId)
    if milestoneData:
        db.session.delete()
        db.session.commit()
        return True
    return False

