from App.database import db
from App.models import MilestoneData

def add_milestone_data(milestoneName,condition, milestoneUrl = ""):
    new_milestoneData = MilestoneData(milestoneName = milestoneName,condition = condition, milestoneUrl= milestoneUrl)
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

# Loads Milestone data into the Database
def load_milestone_data():

    # Equipment Milestones
    # 1
    add_milestone_data("Every problem is a Nail!", "Awarded for owning 1 Gym Equipment","https://i.ibb.co/dG0MGdF/clipart-gym-equipment-4.png")
    # 2
    add_milestone_data("Equipment Einthusiast", "Awarded for owning 5 Gym Equipment","https://i.ibb.co/mqhf7zR/motivated-2x.png")
    #3
    add_milestone_data("Gym Fanatic", "Awarded for owning 10 Gym Equipment","https://i.ibb.co/nDxtfXy/500-F-119148762-ej2q4sy-ONHVelrtbj-C9q-Iqh-G8-GTRw-Py-Q.jpg")
    # 4
    add_milestone_data("The living Gym!","Awarded for owning all Gym Equipment","https://i.ibb.co/pvPtJhS/OIP-2.jpg")

    # Workout Milestones
    # 5
    add_milestone_data("Fresh Meat","Awarded for creating a JustGym account","https://i.ibb.co/pyqVq1T/Logged-in.jpg")
    # 6
    add_milestone_data("Getting Started","Created your first Workout","https://i.ibb.co/5KL6zDt/body-building-clip-art-20.jpg")
    # 7
    add_milestone_data("1 + 1 = 2","Created your 2nd Workout", "https://i.ibb.co/WP7ccC2/2-day-milestone.png")
    # 8
    add_milestone_data("Getting Jacked!","Created your 5th Workout","https://i.ibb.co/bPw05fQ/attachment-128659618.png")

    # Exercise Milestones
    # 9
    add_milestone_data("Let's get pumpin'","Added your first exercise to a workout", "https://i.ibb.co/8XzFY3w/biceps-clipart-5.gif")
  
    # 10
    add_milestone_data("Workout Junkie", "Added 5 exercises to a workout", "https://i.ibb.co/FYLp1RH/OIP-3.jpg")
    # 11
    add_milestone_data("Call me The ROCK!", "Added 10 exercises to a single workout", "https://i.ibb.co/M8JCyy5/the-rock-vector-paint-by-xnitroz-d4rg07h-fullview.png")
    # 12
    add_milestone_data("Greek GOD!", "Added 20 exercises to a single workout", "https://i.ibb.co/xqv47tq/179-1796315-bodybuilder-clip-art-transparent-cartoon-muscle-man-hd.png")
    # 13
    add_milestone_data("Do you even lift, bro?","Added your first Arm exercise.", "https://i.ibb.co/XpD90Pk/R.png")
    
    # Community Milestones
    # 14
    add_milestone_data("I'm something of a professional", "Added your first Workout to the community", "https://i.ibb.co/3yqLDNP/OIP-1.jpg")
    # 15
    add_milestone_data("Mr. Worldwide/Ms. Worldwide","Awarded for adding 5 workouts to the community","https://i.ibb.co/vkWcjXw/login-milestone.png")
    # 16
    add_milestone_data("Calling in the Big guns.", "Awarded for bookmarking your first workout from the community.", "https://i.ibb.co/Y7rYm38/Sports-Weight-Room-Etiquette5-Elham-Numan.jpg")

    # BMI
    # 17
    add_milestone_data("Physically Fit!","Awarded for having a healthy BMI", "https://i.ibb.co/1GkRrYy/arms.jpg")
