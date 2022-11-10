from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import (LoginManager, login_manager, login_user, logout_user, login_required, UserMixin)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'secretkey'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique = True, nullable = False)
    username = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String(80), nullable = False)

with app.app_context():
    db.create_all()

@login_manager.user_loader
@app.route('/user/signin', methods = ['POST'])
def do_signin():
    if(request.method == 'POST'): 
        req = request.get_json()
        password = req['password']
        email = req['email']
        check_user = User.query.filter_by(email=email).first()
        # print(email, password)
        print(check_user)
        if(check_user is not None):
            if(check_user.password == password):
                login_user(check_user) 
                return "LOGGED in successfully"
            else:
                return "Incorrect Password"

        else:
            return "No such User exists"


@app.route('/user/signup', methods = ['POST'])
def do_signup():
    if(request.method == 'POST'): 
        req = request.get_json()
        username = req['username']
        password = req['password']
        email = req['email']
        check_user = User.query.filter_by(email=email).first()
        if(check_user is None):
            newuser = User(
                username=username,
                email=email,
                password=password,
            )
            db.session.add(newuser)
            db.session.commit()
            return "Account successfully created"
        else:
            return "User already exists"

@app.route('/user/signout', methods = ['GET'])
def do_signout():
    if(request.method == 'GET'): 
        logout_user()
        return "Logged Out Successfully"


if "__main__" == __name__:
    app.run(host="127.0.0.1", port="8000", debug=True)