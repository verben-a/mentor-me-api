from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from flask_login import UserMixin


class User(Base):
	"""ONE ----> to """
	"""docstring for User"""
	__tablename__ = "users"
	id = Column(Integer, primary_key=True)
	email = Column(String(128), unique=True)
	password = Column(String(128))
	roles = Column(Boolean)
	# roles = relationship("Role", backref = "users")

	profile = relationship("Profile", uselist=False, backref="profiles")

# class Role(Base):
# 	"""docstring for role"""
# 	__tablename__= "roles"
# 	id = Column(Integer, primary_key=True)
# 	roletype = Column(String(100), default = "mentee")
# 	""".... MANY """
# 	user_id = Column(Integer, ForeignKey('users.id'), nullable = False)

class Profile(Base):
	"""docstring for Profile

	ONE -_ > relationship"""
	__tablename__ = "profiles"

	id = Column(Integer, primary_key=True)
	name_surname = Column(String(100))
	summary = Column(String(128))
	position_at_company = Column(String(300)) 
	experience = relationship("Experience", backref="experiences")
	education = relationship("Education", backref="educations") 
	location = Column(String(100))
	languages = relationship("Language", backref="languages")
	skills = relationship("Skill", backref="skills")
	photo = Column(String(300))
	service = relationship("Service", backref="services")
	linkedin = Column(String(300))
	facebook = Column(String(300))

	user_id = Column(Integer, ForeignKey('users.id'), nullable = False)
		

class Experience(Base):
	"""docstring for Position"""
	__tablename__= "experiences"

	id = Column(Integer, primary_key=True)
	company_name = Column(String(100))
	position_name = Column(String(100))
	position_summary = Column(String(300))

	profile_id = Column(Integer, ForeignKey("experiences.id"), nullable=False)

class Education(Base):
	"""docstring for education"""
	__tablename__= "educations"

	id = Column(Integer, primary_key=True)
	university_name = Column(String(300))
	major_name = Column(String(300))
	education_summary = Column(String(400))

	profile_id = Column(Integer, ForeignKey("educations.id"), nullable=False)

class Language(Base):
	"""docstring for Language"""
	__tablename__="languages"

	id = Column(Integer, primary_key=True)
	language_name = Column(String(50))

	profile_id = Column(Integer, ForeignKey("languages.id"), nullable=False)

class Skill(Base):
	"""docstring for Skill"""
	__tablename__="skills"

	id = Column(Integer, primary_key=True)
	skill_name = Column(String(70))

	profile_id = Column(Integer, ForeignKey("skills.id"), nullable=False)

class Service(Base):
	"""docstring for Service"""
	__tablename__="services"

	id = Column(Integer, primary_key=True)
	service_name = Column(String(50))
	cost = Column(Integer)

	profile_id = Column(Integer, ForeignKey("service.id"), nullable=False)


	
		

