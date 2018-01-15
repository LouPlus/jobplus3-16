from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField
from wtforms.validators import Length, Email, EqualTo, Required
from jobplus.models import db, User, Company
from wtforms import ValidationError



PEOPLE_CHOICES = [('1','1-50'),('2','51-100'),('3','101-500'),('4','>500')]
class Base(FlaskForm):
    __abstract__ = True
    username = StringField('Username', validators=[Required(), Length(3, 24)])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('Password again', validators=[Required(), EqualTo('password')])

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("User already exists")
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')

class CompanyRegisterForm(Base):

    companyName = StringField('Company Name', validators=[Required(), Length(1,100)])
    location = StringField('Location', validators=[Required()])
    number_of_people = SelectField('Number of People', choices = PEOPLE_CHOICES)
    submit = SubmitField('Submit')

    def create_companyProfile(self):
        user = User()
        company = Company()
        company.location = self.location.data
        company.number_of_people = dict(PEOPLE_CHOICES).get(self.number_of_people.data)

        company.save()
        user.company_id = company.id
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        user.realName = self.companyName.data
        user.save()

class UserRegisterForm(Base):
    submit = SubmitField('Submit')

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        user.save()

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')