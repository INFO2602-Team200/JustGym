from App.database import db

class ExerciseData (db.Model):

    id = db.Column(db.Integer, primary_key = True)
    bodyPart = db.Column(db.String(120) , default = '-')
    equipment = db.Column(db.String(120), default = '-')
    gifUrl = db.Column(db.String)
    name = db.Column(db.String)
    target = db.Column(db.String)

    def __init__(self, bodyPart, equipment, gifUrl, name, target):
        self.bodyPart = bodyPart
        self.equipment = equipment
        self.gifUrl = gifUrl
        self.name = name
        self.target = target

    def __repr__(self):
        return f'<ExerciseData id={self.id} name={self.name}>'

    def get_json (self):
        return{
            'id': self.id,
            'bodyPart': self.bodyPart,
            'equipment': self.equipment,
            'gifUrl'  : self.gifUrl,
            'name': self.name,
            'target' : self.target
        }
