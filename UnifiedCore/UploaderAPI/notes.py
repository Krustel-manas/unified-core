# imports
from flask import (request, Blueprint,
                   jsonify, url_for, redirect, flash)
from flask import current_app
import io
from .utils import upload_file_to_cloud
from UnifiedCore import db
from UnifiedCore.models import Notes

# Register this Page as a Blueprint
notes = Blueprint('notes', __name__,)


@notes.route('/')
def alerthome():
    return "NOTES UPLOAD"


@notes.route("/upload_notes", methods=['GET', 'POST'])
def upload_notes():
    try:
        if(request.method == 'POST'):
            # Getting Form Elements
            notes_name = request.form['notes_name']
            topic = request.form['topic']
            subject = request.form['subject']
            grade = request.form['grade']
            notes = request.files['file']

            # Converting the files into bytes
            notesBytes = io.BytesIO(notes.read())

            # upload notes
            notesURI = upload_file_to_cloud(notesBytes)

            if(notesURI['STATUS'] == 'OK'):
                # Add to Database
                new_video = Notes(
                    notes_name=notes_name,
                    subject=subject,
                    topic=topic,
                    grade=grade,
                    notes_url=notesURI['URI'],
                )
                db.session.add(new_video)
                db.session.commit()
            else:
                raise Exception
    except Exception as e:
        flash('Cannot Upload Notes', 'danger')
        return redirect(url_for('admindashboard.upload_notes'))

    flash('Notes Uploaded Successfully!', 'success')
    return redirect(url_for('admindashboard.upload_notes'))
