import os
import json
from random import randint
from faker import Faker
from jobplus.models import db, User, Company, Job

fake = Faker()

def iter_company():
	yield Company(
		company_name = 'JD',
		location='Beijing',
		number_of_people = '5000'
		)

def iter_jobs():
	company = Company.query.filter_by(company_name = 'JD').first()
	with open(os.path.join(os.path.dirname(__file__), '..','datas','jobs.json'),encoding='utf-8-sig') as f:
		jobs = json.load(f)
		for job in jobs:
			yield Job(
				title = job['name'],
				company = company,
				salary = job['salary'],
				experience = job['experience'],
				release_time = job['create_date']
				)


	
def run():
	#for company in iter_company():
	#	db.session.add(company)
	for job in iter_jobs():
		db.session.add(job)
	try:
		db.session.commit()
	except Exception as e:
		print(e)
		db.session.rollback()


	    
