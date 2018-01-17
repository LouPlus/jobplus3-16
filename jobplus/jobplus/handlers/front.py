from flask import Blueprint, render_template, redirect, url_for
from jobplus.models import Job,User,Company
from jobplus.forms import LoginForm, UserRegisterForm, CompanyRegisterForm
from flask import flash
from flask_login import login_user, logout_user, login_required

front = Blueprint('front', __name__)

@front.route('/')
def index():
    jobs = Job.query.filter().limit(10).all()
    companies = Company.query.filter().limit(10).all()
    return render_template('index.html', jobs=jobs, companies = companies)

@front.route('/companyRegister', methods=['GET', 'POST'])
def company_register():
    form = CompanyRegisterForm()
    if form.validate_on_submit():
        form.create_companyProfile()
        flash("Success!", 'success')
        return redirect(url_for('.login'))
    return render_template('company_register.html', form = form)

@front.route('/userRegister', methods=['GET', 'POST'])
def user_register():
    form = UserRegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash("Success!", 'success')
        return redirect(url_for('.login'))
    return render_template('user_register.html', form  = form)

@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user, form.remember_me.data)
        return redirect(url_for('.index'))
    return render_template('login.html', form = form)

@front.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    flash("You have successfull logged out")
    return redirect(url_for('.index'))
