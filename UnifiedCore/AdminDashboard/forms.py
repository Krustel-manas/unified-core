from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField

class UploadVideoForm(FlaskForm):
    vid_name = StringField('VideoName', validators=[DataRequired()])
    subject = SelectField(
        'Subject',
        choices=[
            ('PHY', 'Physics'),
            ('MAT', 'Mathematics'),
            ('CHEM', 'Chemistry'),
            ('BIO', 'Biology'),
            ('HIS', 'History'),
            ('CIV', 'Civics'),
            ('GEO', 'Geography'),
            ('ENG1', 'English Grammar'),
            ('ENG2', 'English Literature'),
            ('COMP', 'Computer Science'),
            ('PE', 'Physical Education'),
            ('ART', 'Arts'),
            ('LNG', 'Second Language'),
            ('LS', 'Life Skills'),
            ('GK', 'General Knowledge'),
            ('O', 'Others'),
        ]
    )
    topic = StringField('Topic', validators=[DataRequired()])
    description = TextAreaField('VideoDesc', validators=[DataRequired()])
    grade = SelectField(
        'Grade',
        choices=[
            ('A', 'Everyone'),
            ('G1', 'Grade 1'), 
            ('G2', 'Grade 2'),
            ('G3', 'Grade 3'),
            ('G4', 'Grade 4'),
            ('G5', 'Grade 5'),
            ('G6', 'Grade 6'),
            ('G7', 'Grade 7'),
            ('G8', 'Grade 8'),
            ('G9', 'Grade 9'),
            ('G10', 'Grade 10'),
            ('ISC', 'ISC'),
            ('KG', 'KinderGarten'),
            ('P', 'Primary (5 & Below Grade 5)'),
            ('H', 'High School (6 & Above Grade 6)'),
        ]
    )
    file = FileField()
    thumbnail = FileField()
    submit = SubmitField('Upload Video')
    

class UploadSampleQuestionPaper(FlaskForm):
    paper_name = StringField('PaperName', validators=[DataRequired()])
    subject = SelectField(
        'Subject',
        choices=[
            ('PHY', 'Physics'),
            ('MAT', 'Mathematics'),
            ('CHEM', 'Chemistry'),
            ('BIO', 'Biology'),
            ('HIS', 'History & Civics'),
            ('GEO', 'Geography'),
            ('ENG1', 'English Grammar'),
            ('ENG2', 'English Literature'),
            ('COMP', 'Computer Science'),
            ('PE', 'Physical Education'),
            ('LNG', 'Second Language'),
        ]
    )
    grade = SelectField(
        'Grade',
        choices=[
            ('G3', 'Grade 3'),
            ('G4', 'Grade 4'),
            ('G5', 'Grade 5'),
            ('G6', 'Grade 6'),
            ('G7', 'Grade 7'),
            ('G8', 'Grade 8'),
            ('G9', 'Grade 9'),
            ('G10', 'Grade 10'),
            ('ISC', 'ISC'),
        ]
    )
    year = TextAreaField('year', validators=[DataRequired()])
    file = FileField()
    submit = SubmitField('Upload Sample Paper')

class DispatchNotification(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    grade = SelectField(
        'Grade',
        choices=[
            ('A', 'Everyone'),
            ('G1', 'Grade 1'), 
            ('G2', 'Grade 2'),
            ('G3', 'Grade 3'),
            ('G4', 'Grade 4'),
            ('G5', 'Grade 5'),
            ('G6', 'Grade 6'),
            ('G7', 'Grade 7'),
            ('G8', 'Grade 8'),
            ('G9', 'Grade 9'),
            ('G10', 'Grade 10'),
            ('ISC', 'ISC'),
            ('KG', 'KinderGarten'),
            ('P', 'Primary (5 & Below Grade 5)'),
            ('H', 'High School (6 & Above Grade 6)'),
        ]
    )
    submit = SubmitField('Dispatch Notification')

class DispatchCircular(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    grade = SelectField(
        'Grade',
        choices=[
            ('A', 'Everyone'),
            ('G1', 'Grade 1'), 
            ('G2', 'Grade 2'),
            ('G3', 'Grade 3'),
            ('G4', 'Grade 4'),
            ('G5', 'Grade 5'),
            ('G6', 'Grade 6'),
            ('G7', 'Grade 7'),
            ('G8', 'Grade 8'),
            ('G9', 'Grade 9'),
            ('G10', 'Grade 10'),
            ('ISC', 'ISC'),
            ('KG', 'KinderGarten'),
            ('P', 'Primary (5 & Below Grade 5)'),
            ('H', 'High School (6 & Above Grade 6)'),
        ]
    )
    file = FileField()
    submit = SubmitField('Dispatch Circular')

class UploadNotes(FlaskForm):
    notes_name = StringField('NotesName', validators=[DataRequired()])
    subject = SelectField(
        'Subject',
        choices=[
            ('PHY', 'Physics'),
            ('MAT', 'Mathematics'),
            ('CHEM', 'Chemistry'),
            ('BIO', 'Biology'),
            ('HIS', 'History'),
            ('CIV', 'Civics'),
            ('GEO', 'Geography'),
            ('ENG1', 'English Grammar'),
            ('ENG2', 'English Literature'),
            ('COMP', 'Computer Science'),
            ('PE', 'Physical Education'),
            ('LNG', 'Second Language'),
            ('O', 'Others'),
        ]
    )
    topic = StringField('Topic', validators=[DataRequired()])
    grade = SelectField(
        'Grade',
        choices=[
            ('G1', 'Grade 1'), 
            ('G2', 'Grade 2'),
            ('G3', 'Grade 3'),
            ('G4', 'Grade 4'),
            ('G5', 'Grade 5'),
            ('G6', 'Grade 6'),
            ('G7', 'Grade 7'),
            ('G8', 'Grade 8'),
            ('G9', 'Grade 9'),
            ('G10', 'Grade 10'),
            ('ISC', 'ISC'),
        ]
    )
    file = FileField()
    submit = SubmitField('Upload Notes')

class UploadResults(FlaskForm):
    term_name = StringField('TermName', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    file = FileField()
    submit = SubmitField('Upload Result Data')

class UploadAttendance(FlaskForm):
    year = StringField('Year', validators=[DataRequired()])
    file = FileField()
    submit = SubmitField('Upload Attendance Data')

class UploadStudent(FlaskForm):
    file = FileField()
    submit = SubmitField('Upload Student Data')