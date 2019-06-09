from flask import render_template, redirect, url_for, request
from dashboard import dashboard_print

@dashboard_print.route("/home")
def dashboard_home_view():
	title = "Home dashboard"
	return render_template("dashboard/dashboard_home_page.html",title=title)
	

	


