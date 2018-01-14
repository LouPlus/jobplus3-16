from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField
from wtforms.validators import Length, Email, EqualTo, Required



class Base(FlaskForm):
    __abstract__ = True
    username = StringField('Username', validators=[Required(), Length(3, 24)])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('Password again', validators=[Required(), EqualTo('password')])

class CompanyRegisterForm(Base):

    companyName = StringField('CompanyName', validators=[Required(), Length(1,100)])
    location = StringField('Location', validators=[Required()])
    number_of_people = SelectField('Number of People', choices = [('1','1-50'),('2','51-100'),('3','101-500'),('4','>500')])
    submit = SubmitField('Submit')

class UserRegisterForm(Base):
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')