from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from UnifiedCore.config import Config
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	Bootstrap(app)
	#Load UploaderAPI Routes
	from UnifiedCore.UploaderAPI.alerts import alerts
	from UnifiedCore.UploaderAPI.students import students
	from UnifiedCore.UploaderAPI.attendance import attendance
	from UnifiedCore.UploaderAPI.notes import notes
	from UnifiedCore.UploaderAPI.results import results
	from UnifiedCore.UploaderAPI.videos import videos
	from UnifiedCore.UploaderAPI.samplepapers import samplepapers
	#Register UploaderAPI Blueprints
	app.register_blueprint(alerts, url_prefix='/upload/alerts')
	app.register_blueprint(students, url_prefix='/upload/students')
	app.register_blueprint(attendance, url_prefix='/upload/attendance')
	app.register_blueprint(notes, url_prefix='/upload/notes')
	app.register_blueprint(results, url_prefix='/upload/results')
	app.register_blueprint(videos, url_prefix='/upload/videos')
	app.register_blueprint(samplepapers, url_prefix='/upload/samplepapers')

	#Load Main Routes
	from UnifiedCore.Main.routes import main
	#Register Main Routes
	app.register_blueprint(main, url_prefix="/")

	#Load AdminDashboard Routes
	from UnifiedCore.AdminDashboard.routes import admindashboard
	#Register AdminDashboard Routes
	app.register_blueprint(admindashboard, url_prefix='/admindashboard')

	#Load ForwardingAPI Routes
	from UnifiedCore.ForwardingAPI.routes import forwardingAPI
	#Register ForwardingAPI Routes
	app.register_blueprint(forwardingAPI, url_prefix='/api')
	return app