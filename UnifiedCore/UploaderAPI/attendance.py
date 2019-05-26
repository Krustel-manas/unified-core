# imports
from flask import (request, Blueprint,
                   jsonify, url_for, redirect, flash)
from flask import current_app
import io
from .utils import extract_excel_data
from UnifiedCore import db
from UnifiedCore.models import Attendance

# Register this Page as a Blueprint
attendance = Blueprint('attendance', __name__)


@attendance.route('/')
def alerthome():
    return "ATTENDANCE UPLOAD"


@attendance.route("/upload_attendance", methods=['GET', 'POST'])
def upload_attendance():
    try:
        # Getting Form Elements
        academic_year = request.form['year']
        attendance_file = request.files['file']

        # Converting the files into bytes
        attendanceBytes = io.BytesIO(attendance_file.read())

        # Extracting Data from Excel
        all_attendance_records = extract_excel_data("bytes", attendanceBytes)

        # Adding To Database
        if(all_attendance_records['status'] == 'OK'):
            attendance_objects = []
            for record in all_attendance_records['data']:
                new_record = Attendance(
                    student_name=record['student_name'].strip(),
                    grade=record['class'],
                    section=record['section'],
                    total_days=record["total_days"],
                    present_days=record["present_days"],
                    absent_days=record["absent_days"],
                    attendance_percentage=record["attendance_percentage"],
                    status=record['status'],
                    year=academic_year
                )
                attendance_objects.append(new_record)
        else:
            return all_attendance_records
        db.session.bulk_save_objects(attendance_objects)
        db.session.commit()
    except Exception as e:
        flash('Cannot Upload Attendance', 'danger')
        return redirect(url_for('admindashboard.upload_attendance'))
    flash('Attendance Uploaded Successfully!', 'success')
    return redirect(url_for('admindashboard.upload_attendance'))
