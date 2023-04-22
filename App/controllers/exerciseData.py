from App.database import db
import App.models.exerciseData as E

def add_exerciseData(exercise):
    db_exercise = E.ExerciseData(name=exercise['name'], bodyPart=exercise['bodyPart'], equipment=exercise['equipment'], target=exercise['target'], gifUrl=exercise['gifUrl'])
    db.session.add(db_exercise)
    return db_exercise

# returns exerciseData based on its id
def get_exerciseData(id):
    exercise = E.ExerciseData.query.filter_by(id = id).first()
    if exercise:
        return exercise
    return None

def get_exerciseData_json(id):
    exercise = get_exerciseData(id)
    if exercise:
        return exercise.get_json()
    return None

    

def get_all_exercises():
    return E.ExerciseData.query.all()

def get_all_exercises_json():
    exercises = get_all_exercises()
    if not exercises:
        return []
    exerciseList = [ exercise.get_json() for exercise in exercises]
    return exerciseList

def get_all_category_exercises(bodyPart):
    exercises = E.ExerciseData.query.filter_by(bodyPart = bodyPart).all()
    if not exercises:
        return []
    
    return exercises

def get_all_exercise_equipment():
    unique_equipment = []

    # Query the database for all ExerciseData objects
    exercises = get_all_exercises()
    
    # Loop through the exercises and add unique equipment to the list
    for exercise in exercises:
        if exercise.equipment not in unique_equipment:
            unique_equipment.append(exercise.equipment)
    
    return unique_equipment

def get_num_all_exercise_equipment():
    equipment = get_all_exercise_equipment()
    return len(equipment)

# def get_all_categories():
#     unique_categories = []

#     # Query the database for all ExerciseData objects
#     exercises = get_all_exercises()
    
#     # Loop through the exercises and add unique equipment to the list
#     for exercise in exercises:
#         if exercise.bodyPart not in unique_categories:
#             unique_categories.append(exercise.bodyPart)
            
#     print(unique_categories)
#     return unique_categories