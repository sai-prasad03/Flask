from application import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True ,autoincrement = True)
    name = db.Column(db.String(100),index = True,nullable = False)
    password = db.Column(db.String(30),nullable = False)

    def __repr__(self):
        return {
            'name':self.name,
            'password':self.password
        }






