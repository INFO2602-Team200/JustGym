from App.database import db
from App.models import UserPreferences


def getUserPreference(user_id):
    user_preference = UserPreferences.query.filter_by(user_id = user_id).first()
    if user_preference:
        return user_preference
    return None

def get_user_preference_json(user_id):
    user_preference = getUserPreference(user_id)
    if user_preference:
        return user_preference.get_json()
    return None

def addUserPreferences(user_id,darkMode,height_units,weight_units):
    new_user_preference = UserPreferences(user_id = user_id,dark_mode=darkMode, height_units=height_units, weight_units=weight_units)
    db.session.add(new_user_preference)
    db.session.commit()
    return new_user_preference

def modifyUserPreferences(user_id,darkMode,height_units,weight_units):
    modify_user_preference = getUserPreference(user_id)
    if modify_user_preference:
        darkMode = darkMode
        height_units = height_units
        weight_units = weight_units
        db.session.add(modify_user_preference)
        db.session.commit()
        return modify_user_preference
    return None

def deleteUserPreferences(user_id):
    terminated_user_preferences = getUserPreference(user_id)
    if terminated_user_preferences:
        db.session.delete(terminated_user_preferences)
        db.session.commit()
        return True
    return False



