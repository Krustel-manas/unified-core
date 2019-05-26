# imports
from flask import (render_template,request, Blueprint,
				   jsonify, url_for, redirect, flash)
from flask import current_app

# Register this Page as a Blueprint
main = Blueprint('main', __name__)

@main.route("/")
def splashscreen():
	return render_template('splashscreen.html')