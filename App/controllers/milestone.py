from App.database import db
from App.models import Milestone
from datetime import datetime




def add_user_milestone(user_id,milestoneDataId, milestone = []):
    from App.controllers import get_milestoneData
    current_date_time = datetime.now()
    milestone = get_milestoneData(milestoneDataId)

    new_user_milestone = Milestone(user_id = user_id,milestoneDataId = milestoneDataId, milestone = milestone, dateObtained = current_date_time )
    db.session.add(new_user_milestone)
    db.session.commit()
    return new_user_milestone

def get_milestone(milestoneId):
    milestone = Milestone.query.filter_by(milestoneId = milestoneId).first()
    if milestone:
        return milestone
    return None


# this function adds milestones based on certain conditions
def check_milestones(user_id):
    from App.controllers import get_num_workouts,append_user_milestone, check_user_milestone

    if check_user_milestone(user_id,1):
        milestone1 = add_user_milestone(user_id,1)
        append_user_milestone(user_id, milestone1)

    if (get_num_workouts(user_id) > 0) and check_user_milestone(user_id,2):
        milestone2 = add_user_milestone(user_id,2)
        append_user_milestone(user_id, milestone2)
    
    if (get_num_workouts(user_id) > 1) and check_user_milestone(user_id,3):
        milestone3 = add_user_milestone(user_id,3)
        append_user_milestone(user_id, milestone3)




