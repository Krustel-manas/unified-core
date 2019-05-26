# imports
from flask import (request, Blueprint,
                   jsonify, url_for, redirect, flash)
from flask import current_app
import io
from .utils import upload_file_to_cloud
from UnifiedCore import db
from UnifiedCore.models import Notifications, Circulars

# Register this Page as a Blueprint
alerts = Blueprint('alerts', __name__)


@alerts.route('/')
def alerthome():
    return "ALERTS"

# =========================================CIRCULARS========================================


@alerts.route("/create_circular", methods=['POST'])
def create_circular():
    file = request.files['file']
    # Converting the file into bytes
    fileBytes = io.BytesIO(file.read())

    uploaded_document = upload_file_to_cloud(fileBytes)

    if(uploaded_document['STATUS'] == "OK"):
        new_circular = Circulars(
            title=request.form['title'],
            message=request.form['message'],
            grade=request.form['grade'],
            fileURI=uploaded_document['URI']
        )
        db.session.add(new_circular)
        db.session.commit()
    else:
        flash('Cannot Upload Circular', 'danger')
        return redirect(url_for('admindashboard.circularuploadpage'))
    flash('Circular Uploaded Successfully!', 'success')
    return redirect(url_for('admindashboard.dispatch_circular'))

# =========================================NOTIFICATIONS========================================


@alerts.route("/create_notification", methods=['POST'])
def create_notification():
    try:
        new_notification = Notifications(
            title=request.form["title"],
            message=request.form["message"],
            grade=request.form["grade"],
        )
        db.session.add(new_notification)
        db.session.commit()
    except Exception as e:
        flash('Cannot Upload Notification', 'danger')
        return redirect(url_for('admindashboard.notificationuploadpage'))
    flash('Notification Uploaded Successfully!', 'success')
    return redirect(url_for('admindashboard.dispatch_notification'))
