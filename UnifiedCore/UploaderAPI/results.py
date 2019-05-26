# imports
from flask import (request, Blueprint,
                   jsonify, url_for, redirect, flash)
from flask import current_app
import io
from .utils import extract_excel_data
from UnifiedCore import db
from UnifiedCore.models import Results

# Register this Page as a Blueprint
results = Blueprint('results', __name__)


@results.route('/')
def alerthome():
    return "RESULTS UPLOAD"


@results.route("/upload_results", methods=['GET', 'POST'])
def upload_results():

    # Getting Form Elements
    academic_year = request.form['year']
    term_name = request.form['term_name']
    results = request.files['file']

    # Converting the files into bytes
    resultsBytes = io.BytesIO(results.read())

    # Extracting Data from Excel
    all_results = extract_excel_data("bytes", resultsBytes)

    # Adding To Database
    if(all_results['status'] == 'OK'):
        result_objects = []
        for result in all_results['data']:
            new_result = Results(
                student_name=result['student_name'].strip(),
                grade=result['class'],
                section=result['section'],
                roll_no=result['roll. No'],
                physics=result['phy'],
                chemistry=result['chem'],
                maths=result['math'],
                biology=result['bio'],
                hisciv=result['hisciv'],
                geography=result['geo'],
                eng1=result['eng1'],
                eng2=result['eng2'],
                sl=result['sl'],
                ca=result['ca'],
                pe=result['pe'],
                arts=result['art'],
                max_marks=result['max_marks'],
                min_marks=result['min_marks'],
                total=result['total'],
                max_total=result['max_total'],
                min_total=result['min_total'],
                percentage=result['percentage'],
                min_percentage=result['min_percentage'],
                status=result['status'],
                term_name=term_name,
                year=academic_year
            )
            result_objects.append(new_result)
    else:
        flash('Cannot upload Results', 'danger')
        return redirect(url_for('admindashboard.upload_results'))

    db.session.bulk_save_objects(result_objects)
    db.session.commit()

    flash('Results Uploaded Successfully!', 'success')
    return redirect(url_for('admindashboard.upload_results'))
