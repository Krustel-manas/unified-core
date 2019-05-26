# imports
from flask import (request, Blueprint,
				   jsonify, url_for, redirect, flash)
from flask import current_app
import io
from .utils import upload_file_to_cloud
from UnifiedCore import db
from UnifiedCore.models import SamplePapers

# Register this Page as a Blueprint
samplepapers = Blueprint('samplepapers', __name__, subdomain='apiuploader', url_prefix='/samplepapers')

@samplepapers.route('/')
def alerthome():
   return "SAMPLE PAPER UPLOAD"

@samplepapers.route('/upload_samplepaper', methods=['GET', 'POST'])
def upload_sample_paper():
	if(request.method == 'POST'):

		# Get Form Data
		paper_name = request.form['paper_name']
		subject = request.form['subject']
		grade = request.form['grade']
		year = request.form['year']
		paper_file = request.files['file']

		# Converting the files into bytes
		paperBytes = io.BytesIO(paper_file.read())

		# Upload Question Paper
		uploaded_paper = upload_file_to_cloud(paperBytes)

		if(uploaded_paper['STATUS'] == 'OK'):
			# Add to Database
			new_paper = SamplePapers(
				paper_name=paper_name,
				subject=subject,
				grade=grade,
				year=year,
				paper_url=uploaded_paper['URI'],
			)
			db.session.add(new_paper)
			db.session.commit()
		else:
			flash('Cannot Upload Sample Paper', 'danger')
			return redirect(url_for('admindashboard.upload_samplepaper'))
			
	flash('Sample Paper Uploaded Successfully!', 'success')
	return redirect(url_for('admindashboard.upload_samplepaper'))