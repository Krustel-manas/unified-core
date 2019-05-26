# imports
from flask import (render_template, request, Blueprint,
				   jsonify, url_for, redirect, flash)
from flask import current_app
from UnifiedCore.AdminDashboard.forms import (UploadVideoForm, UploadSampleQuestionPaper, DispatchNotification,
DispatchCircular, UploadNotes, UploadResults, UploadAttendance, UploadStudent)

# Register this Page as a Blueprint
admindashboard = Blueprint('admindashboard', __name__)

@admindashboard.route("/home")
def homepage():
	return render_template('main.html', title="Welcome", option="Home")

@admindashboard.route("/upload_video")
def upload_video():
	form = UploadVideoForm()
	return render_template('video.html', title="Upload Video", option="Upload Video", form=form)

@admindashboard.route("/upload_samplepaper")
def upload_samplepaper():
	form = UploadSampleQuestionPaper()
	return render_template('samplepaper.html', title="Upload Sample Paper", option="Upload Sample Question Paper", form=form)

@admindashboard.route("/dispatch_notification")
def dispatch_notification():
	form = DispatchNotification()
	return render_template('notification.html', title="Send Notification", option="Dispatch Notification", form=form)

@admindashboard.route("/dispatch_circular")
def dispatch_circular():
	form = DispatchCircular()
	return render_template('circular.html', title="Send Circular", option="Dispatch Circular", form=form)

@admindashboard.route("/upload_notes")
def upload_notes():
	form = UploadNotes()
	return render_template('notes.html', title="Upload Notes", option=" Upload Notes", form=form)

@admindashboard.route("/upload_results")
def upload_results():
	form = UploadResults()
	return render_template('results.html', title="Upload Results", option=" Upload Results", form=form)


@admindashboard.route("/upload_attendance")
def upload_attendance():
	form = UploadAttendance()
	return render_template('attendance.html', title="Upload Attendance", option=" Upload Attendance", form=form)

@admindashboard.route("/upload_student_user")
def upload_student_user():
	form = UploadStudent()
	return render_template('createstudentuser.html', title="Upload Users", option="Import Users", form=form)