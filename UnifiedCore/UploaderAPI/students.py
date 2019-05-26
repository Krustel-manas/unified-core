# imports
from flask import (request, Blueprint,
                   jsonify, url_for, redirect, flash)
from flask import current_app
import io
from .utils import upload_file_to_cloud, extract_excel_data
from UnifiedCore import db
from UnifiedCore.models import StudentInfo

# Register this Page as a Blueprint
students = Blueprint('students', __name__,
                     subdomain='apiuploader', url_prefix='/students')

@students.route('/')
def alerthome():
    return "STUDENT UPLOAD"


@students.route("/create_student_user", methods=['GET', 'POST'])
def create_student_user():

    # Getting Form Elements
    studentexcelsheet = request.files['file']
    # Converting the files into bytes
    studentBytes = io.BytesIO(studentexcelsheet.read())

    # Extracting Data from Excel
    all_student_records = extract_excel_data("bytes", studentBytes)

    # Adding To Database
    print(all_student_records['status'])
    if(all_student_records['status'] == 'OK'):
        student_objects = []
        for record in all_student_records['data']:
            new_record = StudentInfo(
                student_name=record['student_name'],
                grade=record['class'],
                section=record['section'],
                roll_no=record['roll. No'],
                username=record['username'],
                password=record['password'],
                gender=record['gender'],
                email=record['email'],
                phone=record['phone'],
                country=record['country'],
                state=record['state'],
                city=record['city'],
                address=record['address'],
                dob=record['DOB'],
                security_question=record['security_question'],
                security_answer=record['security_answer'],
            )
            student_objects.append(new_record)
    else:
        flash('Cannot Register Students','danger')
        return redirect(url_for('admindashboard.upload_student_user'))
    db.session.bulk_save_objects(student_objects)
    db.session.commit()
    flash('Students Registered Successfully!','success')
    return redirect(url_for('admindashboard.upload_student_user'))
