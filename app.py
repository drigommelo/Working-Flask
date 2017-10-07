import sys
from flask import Flask,render_template, request, url_for, redirect, flash
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user


app=Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm= LoginManager()
lm.init_app(app)

@lm.user_loader
def load_user(id):
    return User.get(id)

import sys
reload(sys)
sys.setdefaultencoding('UTF8')

class Products(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    name= db.Column (db.String(100),nullable=False)
    description = db.Column (db.String (400), nullable=False)
    value = db.Column (db.Integer,nullable=False)

    def __init__(self, name, description, value):
        self.name = name
        self.user_id = user_id
        self.description = description
        self.value = value

class User(db.Model):
    __tablename__ = "users"

    id = db.Column (db.Integer, primary_key=True)
    email = db.Column (db.String(100), unique=True)
    password = db.Column (db.String(50))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __init__ (self, senha, email):
        self.senha = senha
        self.email = email

db.create_all()

@app.route("/createdb")
def createdb():
    db.create_all()
    return "ok"

@app.route ("/")
@app.route ("/index")
def index ():
    return render_template ("index.html")

@app.route ("/login", methods=["GET", "POST"])
def login ():
     print ("1")
     if request.method == "POST":
        email = (request.form.get("email"))
        password = (request.form.get("password"))
        new_user = User.query.filter_by(email='email', password='password')
        print ("1")
        if request.method == "POST":
            print ("2")
            email = (request.form.get("email"))
            password = (request.form.get("password"))
            new_user = User.query.filter_by(email='email', password='password')
            print ("3")
            if password == password: #new_user.password
                flash("Logged in")
                return redirect(url_for("index"))
                print ("4")
            else :
                flash("Invalid login")
                return redirect(url_for("index"))
        print ("5")
        return render_template("login.html")

@app.route ("/cadastro",methods=["GET", "POST"])
def cadastro ():
    if request.method == "POST":
        email = (request.form.get("email"))
        password = (request.form.get("password"))
        new_user = User(email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        flash ("Cadastro com sucesso")

    return render_template ("cadastro.html")

app.run(debug=True)
