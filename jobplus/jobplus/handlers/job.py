from flask import Blueprint, render_template
from jobplus.models import Job, Company
from flask_login import login_required


job = Blueprint('job', __name__, url_prefix='/jobs')

@job.route('/<int:job_id>')
def detail(job_id):
	job = Job.query.get_or_404(job_id)
	company = job.company
	return render_template('job/detail.html', job=job, company=company)