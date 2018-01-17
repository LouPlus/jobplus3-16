from flask import Blueprint, render_template
from jobplus.models import Job, Company
from flask_login import login_required


company = Blueprint('company', __name__, url_prefix='/companies')

@company.route('/<int:company_id>')
def detail(company_id):
	company = Company.query.get_or_404(company_id)
	jobs = Job.query.filter_by(company_id = company.id)
	return render_template('company/detail.html', jobs=jobs, company=company)