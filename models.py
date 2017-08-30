from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from flask_login import UserMixin


class User(Base):
	"""docstring for User"""
	__tablename__ = "users"
	id = Column(Integer, primary_key=True)
	email = Column(String(128), unique=True)
	password = Column(String(128))
	roles = relationship("Role", backref = "users")

	profile = relationship("Profile", uselist=False, backref="profiles")

class Role(Base):
	"""docstring for role"""
	__tablename__= "roles"
	id = Column(Integer, primary_key=True)
	roletype = Column(String(100), default = "mentee")
	user_id = Column(Integer, ForeignKey('users.id'), nullable = False)

class Profile(Base):
	"""docstring for Profile"""
	__tablename__ = "profiles"

	id = Column(Integer, primary_key=True)
	name_surname = Column(String(100))
	summary = Column(String(128))
	position = Column(String(100))
	experience = Column(String(300))
	education = Column(String(100))
	location = Column(String(100))
	languages = Column(String(100))
	skills = Column(String(300))
	photo = Column(String(300))
	linkedin = Column(String(300))
	facebook = Column(String(300))

	user_id =Column(Integer, ForeignKey('users.id'), nullable = False)
		


