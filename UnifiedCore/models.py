
import datetime
from UnifiedCore import db
from flask import current_app

#ADMIN LOGIN
# class StudentAdmin(db.Model):
# 	...

class Notifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(100))
    title = db.Column(db.String(500))
    message = db.Column(db.String(1000))
    sent_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Notification '{self.title}' for grade '{self.grade}' created on '{self.sent_date}'"


class Circulars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(100))
    title = db.Column(db.String(500))
    message = db.Column(db.String(1000))
    fileURI = db.Column(db.String(1000))
    sent_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Circular '{self.title}' for grade '{self.grade}' created on '{self.sent_date}'"


class Videos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_name = db.Column(db.String(500), unique=True)
    subject = db.Column(db.String(10))
    grade = db.Column(db.String(10))
    topic = db.Column(db.String(400))
    description = db.Column(db.String(1000), unique=True)
    video_url = db.Column(db.String(700), unique=True)
    thumbnail_url = db.Column(db.String(700), unique=True)
    posted_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Video '{self.video_name}' for grade '{self.grade}' created on '{self.posted_date}'"


class SamplePapers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paper_name = db.Column(db.String(500))
    subject = db.Column(db.String(100))
    grade = db.Column(db.String(10))
    paper_url = db.Column(db.String(500))
    year = db.Column(db.String(200))

    def _repr_(self):
        return f"Sample Paper '{self.paper_name}' for grade '{self.grade}' created on '{self.uploaded_date}'"


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes_name = db.Column(db.String(500), unique=True)
    subject = db.Column(db.String(10))
    grade = db.Column(db.String(10))
    topic = db.Column(db.String(400))
    notes_url = db.Column(db.String(700), unique=True)
    posted_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Notes '{self.notes_name}' for grade '{self.grade}' created on '{self.posted_date}'"


class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.PickleType)
    grade = db.Column(db.PickleType)
    section = db.Column(db.PickleType)
    roll_no = db.Column(db.PickleType)
    physics = db.Column(db.PickleType)
    chemistry = db.Column(db.PickleType)
    maths = db.Column(db.PickleType)
    biology = db.Column(db.PickleType)
    hisciv = db.Column(db.PickleType)
    geography = db.Column(db.PickleType)
    eng1 = db.Column(db.PickleType)
    eng2 = db.Column(db.PickleType)
    sl = db.Column(db.PickleType)
    ca = db.Column(db.PickleType, nullable=True)
    pe = db.Column(db.PickleType, nullable=True)
    arts = db.Column(db.PickleType, nullable=True)
    max_marks = db.Column(db.PickleType)
    min_marks = db.Column(db.PickleType)
    max_total = db.Column(db.PickleType)
    min_total = db.Column(db.PickleType)
    total = db.Column(db.PickleType)
    percentage = db.Column(db.PickleType)
    min_percentage = db.Column(db.PickleType)
    status = db.Column(db.PickleType)
    term_name = db.Column(db.PickleType)
    year = db.Column(db.PickleType)

    def __repr__(self):
        return f"{self.student_name}'s Report Card for grade '{self.grade}'."


class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String)
    grade = db.Column(db.PickleType)
    section = db.Column(db.PickleType)
    total_days = db.Column(db.PickleType)
    present_days = db.Column(db.PickleType)
    absent_days = db.Column(db.PickleType)
    attendance_percentage = db.Column(db.PickleType)
    status = db.Column(db.PickleType)
    year = db.Column(db.PickleType)

    def __repr__(self):
        return f"{self.student_name}'s Attendance Report for academic year '{self.year}'."


class StudentInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.PickleType)
    grade = db.Column(db.PickleType)
    section = db.Column(db.PickleType)
    roll_no = db.Column(db.PickleType)
    bio = db.Column(db.PickleType, nullable=True)
    username = db.Column(db.PickleType)
    password = db.Column(db.PickleType)
    gender = db.Column(db.PickleType)
    email = db.Column(db.PickleType)
    phone = db.Column(db.PickleType)
    country = db.Column(db.PickleType)
    state = db.Column(db.PickleType)
    city = db.Column(db.PickleType)
    address = db.Column(db.PickleType)
    dob = db.Column(db.PickleType)
    security_question = db.Column(db.PickleType)
    security_answer = db.Column(db.PickleType)
    posts = db.Column(db.PickleType, nullable=True)
    profile_pic_URL = db.Column(db.PickleType, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Student {self.student_name}'s Account"