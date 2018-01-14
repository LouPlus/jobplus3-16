from flask import Blueprint, render_template
from jobplus.models import Job
from jobplus.forms import LoginForm, UserRegisterForm, CompanyRegisterForm

front = Blueprint('front', __name__)

@front.route('/')
def index():
    jobs = Job.query.all()
    return render_template('index.html', jobs=jobs)

@front.route('/companyRegister')
def company_register():
	form = CompanyRegisterForm()
	return render_template('company_register.html', form = form)

@front.route('/userRegister')
def user_register():
	form = UserRegisterForm()
	return render_template('user_register.html', form  = form)

@front.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', form = form)