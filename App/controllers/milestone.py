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
    from App.controllers import get_num_workouts,append_user_milestone, check_user_milestone,check_exercise_type,get_highest_num_exercises, get_num_userEquipment,get_num_all_exercise_equipment

    if (get_num_userEquipment(user_id) > 0) and check_user_milestone(user_id,1):
        milestone1 = add_user_milestone(user_id,1)
        append_user_milestone(user_id, milestone1)

    if (get_num_userEquipment(user_id) > 4) and check_user_milestone(user_id,2):
        milestone2 = add_user_milestone(user_id,2)
        append_user_milestone(user_id, milestone2) 

    if (get_num_userEquipment(user_id) > 9) and check_user_milestone(user_id,3):
        milestone3 = add_user_milestone(user_id,3)
        append_user_milestone(user_id, milestone3) 

    if (get_num_userEquipment(user_id) == get_num_all_exercise_equipment()) and check_user_milestone(user_id,4):
        milestone4 = add_user_milestone(user_id,4)
        append_user_milestone(user_id, milestone4) 
# ------------------
    if check_user_milestone(user_id,5):
        milestone5 = add_user_milestone(user_id,5)
        append_user_milestone(user_id, milestone5)
   
    if (get_num_workouts(user_id) > 0) and check_user_milestone(user_id,6):
        milestone6 = add_user_milestone(user_id,6)
        append_user_milestone(user_id, milestone6)
    
    if (get_num_workouts(user_id) > 1) and check_user_milestone(user_id,7):
        milestone7 = add_user_milestone(user_id,7)
        append_user_milestone(user_id, milestone7)
    
    if (get_num_workouts(user_id) > 4) and check_user_milestone(user_id,8):
        milestone8 = add_user_milestone(user_id,8)
        append_user_milestone(user_id, milestone8)
# ------------------
    if (get_highest_num_exercises(user_id) > 0) and check_user_milestone(user_id,9):
        milestone9 = add_user_milestone(user_id,9)
        append_user_milestone(user_id, milestone9)

    if (get_highest_num_exercises(user_id) > 4) and check_user_milestone(user_id,10):
        milestone10 = add_user_milestone(user_id,10)
        append_user_milestone(user_id, milestone10)

    if (get_highest_num_exercises(user_id) > 9) and check_user_milestone(user_id,11):
        milestone11 = add_user_milestone(user_id,11)
        append_user_milestone(user_id, milestone11)

    if (get_highest_num_exercises(user_id) > 19) and check_user_milestone(user_id,12):
        milestone12 = add_user_milestone(user_id,12)
        append_user_milestone(user_id, milestone12)

    if (check_exercise_type(user_id,"lower arms") or check_exercise_type(user_id,"upper arms")) and check_user_milestone(user_id,13):
        milestone13 = add_user_milestone(user_id,13)
        append_user_milestone(user_id, milestone13)



