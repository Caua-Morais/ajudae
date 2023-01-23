from utils import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64))

    def __init__(self, name, email, password):
      self.name = name
      self.email = email
      self.password = password
      
    def __repr__(self):
        return '<User{}>'.format(self.username)

class Institution(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), index=True, unique=True)
  address = db.Column(db.String(64), index=True)
  contact = db.Column(db.String(64), index=True)
  email = db.Column(db.String(64), index=True, unique=True)
  password = db.Column(db.String(64))

  def __init__(self, name, email, adress, contact, password):
    self.name = name
    self.email = email
    self.address = adress
    self.contact = contact
    self.password = password
    
  def __repr__(self):
      return '<Instituicao{}>'.format(self.username)