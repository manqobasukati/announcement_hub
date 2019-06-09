#home page 
from flask import render_template
from flask_login import login_required, current_user
from home import home_print


@home_print.route("/home")
@home_print.route("/")
def home_page():
	title = "Welcome to the announcement hub"
	return render_template("home/home_base.html",title=title)
	


@home_print.route("/about")
def about_page():
	title = "about us"
	return render_template("home/about_page.html",title=title)
	
@home_print.route("/team")
def team_page():
	title = "Team"
	return render_template("home/team_page.html",title=title)
