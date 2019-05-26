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
	app = Flask(__name__, subdomain_matching=True)
	app.config.from_object(Config)
	app.url_map.default_subdomain = "app"
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
	app.register_blueprint(alerts)
	app.register_blueprint(students)
	app.register_blueprint(attendance)
	app.register_blueprint(notes)
	app.register_blueprint(results)
	app.register_blueprint(videos)
	app.register_blueprint(samplepapers)

	#Load Main Routes
	from UnifiedCore.Main.routes import main
	#Register Main Routes
	app.register_blueprint(main)

	#Load AdminDashboard Routes
	from UnifiedCore.AdminDashboard.routes import admindashboard
	#Register AdminDashboard Routes
	app.register_blueprint(admindashboard)

	#Load ForwardingAPI Routes
	from UnifiedCore.ForwardingAPI.routes import forwardingAPI
	#Register ForwardingAPI Routes
	app.register_blueprint(forwardingAPI)
	return app