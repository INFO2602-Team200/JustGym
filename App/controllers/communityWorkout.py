from App.database import db
from App.models import communityWorkout
from App.controllers import get_workout

def create_community_workout(workoutID):
    workout = get_workout(workoutID)

    new_community_workout = communityWorkout(communityId = 1, workoutId=workoutID, workout  = workout, upvotes= 0, downvotes=0)
    
    if new_community_workout:
        db.session.add(new_community_workout)
        db.session.commit()
        return new_community_workout
    return None

def get_community_workout(workoutId):
    community_workout = communityWorkout.query.filter_by(workoutId = workoutId).first()  
    if community_workout:
        return community_workout 
    return None

def remove_community_workout(workoutID):
    community_workout = get_community_workout(workoutID)
    if community_workout:
        db.session.delete(community_workout)
        db.session.commit()
        return True
    return False

def calc_net_votes(upvotes,downvotes):
    return upvotes-downvotes

def addVote(communityWorkoutID):
    community_workout = get_community_workout(communityWorkoutID)
    community_workout.upvotes = community_workout.upvotes + 1
    community_workout.netvotes = calc_net_votes(community_workout.upvotes, community_workout.downvotes)
    if community_workout:
        db.session.add(community_workout)
        db.session.commit()
        return community_workout
    return None

def addDownVote(communityWorkoutID):
    community_workout = get_community_workout(communityWorkoutID)
    community_workout.downvotes = community_workout.downvotes + 1
    community_workout.netvotes = calc_net_votes(community_workout.upvotes, community_workout.downvotes)
    if community_workout:
        db.session.add(community_workout)
        db.session.commit()
        return community_workout
    return None

