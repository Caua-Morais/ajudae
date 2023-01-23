from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from flask_login import login_user, login_required
from utils import db, lm, map_html
from models import User, Institution



app = Flask(__name__)
app.secret_key =  's6uS6^D#49g@'
app.config
migrate = Migrate(app, db)
conexao = "sqlite:///app.db"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
lm.init_app(app)

@lm.user_loader
def load_user(id):
    return User.query.get(id)

@app.route('/')
def index():
    return render_template('home.html', mapc=map_html)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
  if request.method=="GET":
    return render_template('cadastro.html')

  # Catch the data from the request form and register
  name = request.form.get('name')
  email = request.form.get('email')
  password = request.form.get('pass')

  user = User(name, email, password)
  
  db.session.add(user)
  db.session.commit()
  return redirect('/login')
  
@app.route('/login', methods=["GET", "POST"])
def login():
  if request.method == "GET":
    return render_template('login.html')

  # Catch the data from the request form and log
  email = request.form.get('email')
  password = request.form.get('password')
  user = User.query.filter_by(email = email).first()

  if password != user.password:
    redirect('/')
    
  login_user(user)
  return redirect(f'/user/{user.id}')

@login_required
@app.route('/user/<int:id>')
def userInfos(id):
  user = User.query.filter_by(id = id).first()
  return render_template('user.html', user=user)

@app.route('/instituicao-cad', methods=["GET", "POST"])
def instCad():
  if request.method == "GET":
    return render_template('instituicao_cadastro.html')

  # Catch the data from the request form and register
  name = request.form.get('name')
  email = request.form.get('email')
  address = request.form.get('address')
  contact = request.form.get('contact')
  password = request.form.get('pass')

  institution = Institution(name, email, address, contact, password)
  db.session.add(institution)
  db.session.commit()

  return redirect('/instituicao-login')
  

@app.route('/instituicao-login', methods=["GET", "POST"])
def instLogin():
  if request.method ==  "GET":
    return render_template('login.html')

  # Catch the data from the request form and log
  email = request.form.get('email')
  password = request.form.get('pass')
  institution = Institution.query.filter_by(email = email).first()

  if password != Institution.password:
    redirect('/')
    
  login_user(institution)
  return redirect(f'/institution-infos/{institution.id}')

@login_required
@app.route('/institution-infos/<int:id>')
def instInfos(id):
  institution = Institution.query.filter_by(id=id).first()
  return render_template('inst_infos.html', institution=institution)

app.run(host='0.0.0.0', port=81)