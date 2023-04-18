from App.database import db
from App.models import Community

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


# def netVotes(workout):
#     return workout['netvotes']

