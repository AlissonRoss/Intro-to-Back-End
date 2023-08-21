from app import db

# This is where you will define all your database classes.

class User(db.Model):
    __tablename__= "user"

    #we are creating a table of data here
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=False, nullable=False)
    #CONSTRUCTORS
    #self === this
    #double underscore is a dunner
    def __init__(self, name):
        self.name = name
    def get_user(lookupName):
        user = User.query.filter_by(name=lookupName).first()
        return user
