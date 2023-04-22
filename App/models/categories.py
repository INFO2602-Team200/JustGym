from App.database import db

class Categories (db.Model):

    categoryId = db.Column(db.Integer, primary_key = True)
    categoryName = db.Column(db.String(120) , default = '-')
    categoryImgUrl = db.Column(db.String, default = '-')
    
    def __init__(self, categoryName, categoryImgUrl):
        self.categoryName = categoryName
        self.categoryImgUrl = categoryImgUrl

    def get_json(self):
        return {
        'categoryName': self.categoryName,
        'categoryImgUrl': self.categoryImgUrl,
        }