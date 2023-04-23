from App.database import db
from App.models import Community
from flask_login import current_user

def add_community(communityWorkout = []):
    community = Community(communityWorkout = communityWorkout)
    if community:
        db.session.add(community)
        db.session.commit()
        return community
    return None

def get_community(communityId):
    community = Community.query.filter_by(communityId = communityId).first()
    return community

# add community workout to community list
def add_community_workout(communityId, communityWorkout):
    community = get_community(communityId)
    if community:
        community.communityWorkout.append(communityWorkout)
        community.communityWorkout.sort(reverse = True, key = lambda workout: workout.netvotes)
        db.session.add(community)
        db.session.commit()
        return True
    return False

# remove community workout from community list
def delete_community_workout(communityId, workoutId):
    from App.controllers import get_community_workout

    community = get_community(communityId)
    if community:
        community_workout = get_community_workout(workoutId)
        community.communityWorkout.remove(community_workout)
        db.session.add(community)
        db.session.commit()
        return True
    return False


def copy_Workout(workoutId):
    from App.controllers import get_workout, add_copy_workout
    original_workout = get_workout(workoutId)
    if original_workout:
        copied_workout = add_copy_workout(current_user.id,original_workout.workoutName,False,original_workout.categoryId,original_workout.category,original_workout.workoutExercises,original_workout.estimatedDuration, original_workout.author)
        db.session.add(copied_workout)
        db.session.commit()
        return True
    return False



# def netVotes(workout):
#     return workout['netvotes']

