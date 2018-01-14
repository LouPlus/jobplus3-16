#data model file
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)

#Status code: 1-active, 2-inprogress, 3-pass, 4-denied
applications = db.Table('applications', db.Column('user_id',db.Integer, db.ForeignKey('user.id'), primary_key=True),
                                        db.Column('job_id', db.Integer, db.ForeignKey('job.id'), primary_key=True),
                                        db.Column('status', db.Integer),
                                        db.Column('created_at', db.DateTime, default = datetime.utcnow)
                                        )


# Handle Cover all user type in jobplus
class User(Base, UserMixin):
    __tablename__ = 'user'

    ROLE_USER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key = True)
    company_id = db.Column(db.Integer,db.ForeignKey('company.id',ondelete='SET NULL'))
    company = db.relationship('Company',uselist = False)
    description = db.Column(db.String(256))
    username = db.Column(db.String(32), unique = True, index=True, nullable = False)
    email = db.Column(db.String(64), unique = True, index=True, nullable = False)
    _password = db.Column("password", db.String(256), nullable=False) # the first argument can be an optional string to represent a different name
    role = db.Column(db.SmallInteger, default= ROLE_USER)
    resumeId = db.Column(db.Integer, unique=True) #1/13/18 Can I change flask config to customize stored folder name?
    realName = db.Column(db.String(64))
    phoneNumber = db.Column(db.Integer)
    applied_jobs = db.relationship('job', secondary=applications, lazy='subquery', backref=db.backref('users',lazy=True)),
    active = db.Column(db.Boolean, default = True)

    def __repr__(self):
        return '<User:{}>'.format(self.username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_company(self):
        return self.role == self.ROLE_COMPANY


class Company(Base):
    __tablename__ = 'company'
    
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(256))
    location = db.Column(db.String(32), nullable = False)
    number_of_people = db.Column(db.String(32), nullable = False)
    published_job = db.relationship('Job')
    url = db.Column(db.String(256))
    full_description = db.Column(db.String(256))

class Job(Base):
    __tablename__ = 'job'

    id = db.Column(db.Integer,primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id', ondelete = 'SET NULL'))
    company = db.relationship('Company', uselist=False)
    title = db.Column(db.String(32))
    description = db.Column(db.String(256))
    salary = db.Column(db.String(32))
    experience = db.Column(db.String(32))
    education = db.Column(db.String(32))
    location = db.Column(db.String(32))
    number = db.Column(db.Integer)
    active = db.Column(db.Boolean, default = True)











