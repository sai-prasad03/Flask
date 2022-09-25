from flask import Blueprint
from flask import render_template,request,redirect
from application.user.models import Student
from application import db

mod = Blueprint('user', __name__)


@mod.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@mod.route('/create_user',methods = ['POST'])
def Create_user():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        entry = Student(name=name,password=password)
        db.session.add(entry)
        db.session.commit()
        return "user added"

@mod.route('/fetch',methods = ['GET'])

def fetch_user():
    user = Student.query.all()
    user_details = [x.__repr__() for x in user]
    return user_details

@mod.route('/log',methods = ['GET','POST'])
def log():
    return render_template("login.html")

@mod.route('/login',methods=['GET','POST'])
def Login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        user = Student.query.filter(Student.name == name).first()
        try:
            if user.name == name and user.password == password:
                return "<h2>logged successfull</h2>"
            else:
                return "please provide valid password"
        except Exception as e:
            return 'please provide valid name'

        return render_template('home.html')


