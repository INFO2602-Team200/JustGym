from App.database import db
from App.models import Categories


def add_category(categoryName, categoryImgUrl):
    new_category = Categories(categoryName= categoryName, categoryImgUrl= categoryImgUrl)
    db.session.add(new_category)
    db.session.commit()

def get_category(categoryId):
    category = Categories.query.filter_by(categoryId = categoryId).first()
    if category:
        return category
    return None

def get_category_json(categoryId):
    category = Categories.query.filter_by(categoryId = categoryId).first()
    if category:
        return category.get_json()
    return None

def load_categories():
    add_category("back","../static/catImages/back.jpg")
    add_category("cardio","../static/catImages/cardio.jpg")
    add_category("chest","../static/catImages/chest.jpg")
    add_category("lower arms","../static/catImages/lowerarms.jpg")
    add_category("lower legs","../static/catImages/lowerlegs.jpg")
    add_category("neck","../static/catImages/neck.jpg")
    add_category("shoulders","../static/catImages/shoulders.jpg")
    add_category("upper arms","../static/catImages/upperarms.jpg")
    add_category("upper legs","../static/catImages/upperlegs.jpg")
    add_category("waist","../static/catImages/waist.jpg")

def get_all_categories():
    categories = Categories.query.all()
    return categories