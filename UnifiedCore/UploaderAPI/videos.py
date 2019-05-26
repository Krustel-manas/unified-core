# imports
from flask import (request, Blueprint,
				   jsonify, url_for, redirect, flash)
from flask import current_app
import io
from .utils import upload_file_to_cloud
from UnifiedCore import db
from UnifiedCore.models import Videos

# Register this Page as a Blueprint
videos = Blueprint('videos', __name__)


@videos.route('/')
def alerthome():
	return "VIDEO UPLOAD"

@videos.route("/upload_video", methods=['GET', 'POST'])
def upload_video():
	try:
		if(request.method == 'POST'):
			# Getting Form Elements
			video_name = request.form['vid_name']
			topic = request.form['topic']
			subject = request.form['subject']
			grade = request.form['grade']
			desc = request.form['description']
			vid = request.files['file']
			thumbnail = request.files['thumbnail']

			# Converting the files into bytes
			videoBytes = io.BytesIO(vid.read())
			thumbnailBytes = io.BytesIO(thumbnail.read())

			# upload video
			uploaded_video = upload_file_to_cloud(videoBytes, 'video')
			# upload image
			uploaded_thumbnail = upload_file_to_cloud(thumbnailBytes)

			if(uploaded_video['STATUS'] == 'OK' and uploaded_thumbnail['STATUS'] == 'OK'):
				# Add to Database
				new_video = Videos(
					video_name=video_name,
					subject=subject,
					topic=topic,
					grade=grade,
					description=desc,
					video_url=uploaded_video['URI'],
					thumbnail_url=uploaded_thumbnail['URI']
				)
				db.session.add(new_video)
				db.session.commit()
			else:
				flash('Cannot Upload Video', 'danger')
				return redirect(url_for('admindashboard.upload_video'))
	except Exception as e:
		print(e)
		flash('Cannot Upload Video', 'danger')
		return redirect(url_for('admindashboard.upload_video'))

	flash('Video Uploaded Successfully!', 'success')
	return redirect(url_for('admindashboard.upload_video'))
