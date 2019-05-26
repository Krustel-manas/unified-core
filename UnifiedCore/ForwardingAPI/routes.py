# imports
from flask import (request, Blueprint,
                   jsonify, url_for, redirect, flash)
from flask import current_app
from UnifiedCore import db
from UnifiedCore.models import (
    Notifications, Circulars, Videos, SamplePapers, Notes, Results, Attendance, StudentInfo)

# Register this Page as a Blueprint
forwardingAPI = Blueprint('forwardingAPI', __name__)


@forwardingAPI.route('/')
def alerthome():
    return "forwardingAPI"

#                                    ----NOTIFICATIONS----
@forwardingAPI.route("/notificationbyid/<id>", methods=['GET'])
def getnotificationbyname(id):
    notification = Notifications.query.filter_by(id=id).first()
    rx = {
        "id": notification.id,
        "title":  notification.title,
        "message": notification.message,
        "grade": str(notification.grade),
        "sent_date": notification.sent_date
    }
    return jsonify({
        "response": rx
    })

# GET


@forwardingAPI.route("/notificationsbygrade/<grade>", methods=['GET'])
def getnotificationsbygrade(grade):
    n = []
    notifications = Notifications.query.filter_by(grade=grade).all()
    globalnotifications = Notifications.query.filter_by(grade="A").all()
    for notification in notifications:
        rx = {
            "id": notification.id,
            "title":  notification.title,
            "message": notification.message,
            "grade": str(notification.grade),
            "sent_date": notification.sent_date
        }
        n.append(rx)
    for gnotification in globalnotifications:
        rx = {
            "id": gnotification.id,
            "title":  gnotification.title,
            "message": gnotification.message,
            "grade": str(gnotification.grade),
            "sent_date": gnotification.sent_date
        }
        n.append(rx)
    return jsonify({
        "response": n
    })


#                                       ----CIRCULARS----

@forwardingAPI.route("/circularbyid/<id>", methods=['GET'])
def getcircularbyname(id):
    circular = Circulars.query.filter_by(id=id).first()
    rx = {
        "title":  circular.title,
        "message": circular.message,
        "documentURI": circular.fileURI,
        "sent_date": circular.sent_date
    }
    return jsonify({
        "response": rx
    })


@forwardingAPI.route("/circularsbygrade/<grade>", methods=['GET'])
def getcircularssbygrade(grade):
    r = []
    c = Circulars.query.filter_by(grade=grade).all()
    globalc = Circulars.query.filter_by(grade="A").all()
    for circular in c:
        rx = {
            "id": circular.id,
            "title":  circular.title,
            "message": circular.message,
            "documentURI": circular.fileURI,
            "sent_date": circular.sent_date
        }
        r.append(rx)
    for gcircular in globalc:
        rx = {
            "id": gcircular.id,
            "title":  gcircular.title,
            "message": gcircular.message,
            "documentURI": gcircular.fileURI,
            "sent_date": gcircular.sent_date
        }
        r.append(rx)
    return jsonify({
        "response": r
    })

#                                       ----VIDEOS----


@forwardingAPI.route("/videosbytopic/<topic>", methods=['GET'])
def videosbytopic(topic):
    v = []
    videos = Videos.query.filter_by(topic=topic).all()
    for video in videos:
        rx = {
            'video_name': video.video_name,
            'topic': video.topic,
            'subject': video.subject,
            'grade': str(video.grade),
            'description': video.description,
            'thumbnailURI': video.thumbnail_url,
            'videoURI': video.video_url
        }
        v.append(rx)
    return jsonify({
        "response": v
    })


@forwardingAPI.route("/videobyname/<name>", methods=['GET'])
def getvideobyname(name):
    video = Videos.query.filter_by(video_name=name).first()
    rx = {
        'video_name': video.video_name,
        'topic': video.topic,
        'subject': video.subject,
        'grade': str(video.grade),
        'description': video.description,
        'thumbnailURI': video.thumbnail_url,
        'videoURI': video.video_url
    }
    return jsonify({
        "response": rx
    })


@forwardingAPI.route("/videos/<grade>", methods=['GET'])
def gradedvideo(grade):
    v = []
    gradedvideos = Videos.query.filter_by(grade=grade).all()
    publicvideos = Videos.query.filter_by(grade="A").all()
    # Returns Specific Grade Videos
    for video in gradedvideos:
        rx = {
            'video_name': video.video_name,
            'topic': video.topic,
            'subject': video.subject,
            'grade': str(video.grade),
            'description': video.description,
            'thumbnailURI': video.thumbnail_url,
            'videoURI': video.video_url
        }
        v.append(rx)
    # Returns Videos Marked as All Grades.
    for pvideo in publicvideos:
        rx = {
            'video_name': pvideo.video_name,
            'topic': pvideo.topic,
            'subject': pvideo.subject,
            'grade': str(video.grade),
            'description': pvideo.description,
            'thumbnailURI': pvideo.thumbnail_url,
            'videoURI': pvideo.video_url
        }
        v.append(rx)
    return jsonify({
        "response": v
    })

    @forwardingAPI.route("/topics/<grade>/<subject>")
    def returntopics(grade, subject):
        topics = set()
        all_vids = Videos.query.filter_by(subject=subject, grade="A").all()
        graded_vids = Videos.query.filter_by(
            subject=subject, grade=grade).all()
        for video in all_vids:
            topics.add(video.topic)
        for gvideo in graded_vids:
            topics.add(gvideo.topic)
        return jsonify({
            "response": list(topics)
        })

#                                   ----SAMPLE PAPERS------


@forwardingAPI.route('/samplepapers/<grade>/<subject>')
def samplepapersbygradeandsubject(grade, subject):
    p = []
    sample_papers = SamplePapers.query.filter_by(
        grade=grade, subject=subject).all()
    for sample_paper in sample_papers:
        rx = {
            'paper_name': sample_paper.paper_name,
            'subject': sample_paper.subject,
            'grade': str(sample_paper.grade),
            'paper_url': sample_paper.paper_url,
            'year': str(sample_paper.year),
        }
        p.append(rx)
    return jsonify({
        "response": p
    })

#                                 ----NOTES----


@forwardingAPI.route("/notes/<grade>/<subject>", methods=['GET'])
def notesbygradeandsubject(grade, subject):
    n = []
    all_notes = Notes.query.filter_by(grade=grade, subject=subject).all()
    for notes in all_notes:
        rx = {
            'notes_name': notes.notes_name,
            'topic': notes.topic,
            'subject': notes.subject,
            'grade': str(notes.grade),
            'notesURI': notes.notes_url
        }
        n.append(rx)
    return jsonify({
        "response": n
    })


@forwardingAPI.route("/topics/<grade>/<subject>")
def returntopics(grade, subject):
    topics = set()
    all_vids = Videos.query.filter_by(subject=subject, grade="A").all()
    graded_vids = Videos.query.filter_by(subject=subject, grade=grade).all()
    for video in all_vids:
        topics.add(video.topic)
    for gvideo in graded_vids:
        topics.add(gvideo.topic)
    return jsonify({
        "response": list(topics)
    })

#                                -----ATTENDANCE----


@forwardingAPI.route("/attendance/<year>/<student_name>", methods=['GET'])
def specific_attendance_record(year, student_name):
    student_name = student_name.strip().upper()
    record = Attendance.query.filter_by(
        year=year, student_name=student_name).first()
    return jsonify({
        "student_name": str(record.student_name).strip(),
        "grade": str(record.grade),
        "section": str(record.section[0]),
        "total_days": str(record.total_days),
        "present_days": str(record.present_days),
        "absent_days": str(record.absent_days),
        "attendance_percentage": str(record.attendance_percentage),
        "status": str(record.status),
        "year": str(record.year)
    })

#                              -----RESULTS-----


@forwardingAPI.route("/results/<year>/<term_name>/<student_name>", methods=['GET'])
def specific_results(year, term_name, student_name):
    student_name = student_name.upper()
    result = Results.query.filter_by(
        year=year, term_name=term_name, student_name=(student_name,)).first()
    return jsonify({
        "student_name": result.student_name[0].strip(),
        "grade": str(result.grade[0]),
        "section": str(result.section[0]),
        "roll_no": str(result.roll_no[0]),
        "physics": str(result.physics[0]),
        "chemistry": str(result.chemistry[0]),
        "maths": str(result.maths[0]),
        "biology": str(result.biology[0]),
        "hisciv": str(result.hisciv[0]),
        "geography": str(result.geography[0]),
        "eng1": str(result.eng1[0]),
        "eng2": str(result.eng2),
        "sl": str(result.sl),
        "ca": str(result.ca[0]),
        "pe": str(result.pe[0]),
        "arts": str(result.arts[0]),
        "max_marks": str(result.max_marks[0]),
        "min_marks": str(result.min_marks[0]),
        "max_total": str(result.max_total[0]),
        "min_total": str(result.min_total[0]),
        "total": str(result.total[0]),
        "percentage": str(result.percentage[0]),
        "min_percentage": str(result.min_percentage),
        "status": str(result.status[0]),
        "term_name": str(result.term_name),
        "year": str(result.year),
    })

#                                     ----STUDENT LOGIN----


@forwardingAPI.route("/studentlogin/<username>/<password>", methods=['POST'])
def specific_student_user_record(username, password):
    username, password = username.upper(), password.upper()
    student_record = StudentInfo.query.filter_by(
        username=username, password=password).first()
    # CHECK IF LOGIN IS CORRECT
    if(student_record):
        student_info = {
            "student_name": student_record.student_name.strip(),
            "grade": str(student_record.grade),
            "section": str(student_record.section),
            "roll_no": str(student_record.roll_no),
            "username": str(student_record.username),
            "gender": str(student_record.gender),
            "email": str(student_record.email),
            "phone": str(student_record.phone),
            "country": str(student_record.country),
            "state": str(student_record.state),
            "city": str(student_record.city),
            "address": str(student_record.address),
            "dob": str(student_record.dob),
            "security_question": str(student_record.security_question),
            "security_answer": str(student_record.security_answer),
            "bio": str(student_record.bio),
            "profile_pic": str(student_record.profile_pic_URL),
            "posts": str(student_record.posts)
        }
        return jsonify({
            "response": {
                "CODE": "OK",
                "INFO": student_info
            }
        })
    else:
        return jsonify({
            "response": {
                "CODE": "INCORRECT CREDENTIALS",
            }
        })

#                                   -----GENERAL GETTERS-----
