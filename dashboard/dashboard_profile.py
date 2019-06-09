from flask import render_template, redirect, url_for, request
from flask_login import login_required
from dashboard import dashboard_print
from models import Media


@dashboard_print.route("/profile")
@login_required
def dashboard_profile_view(current_user):
	title = "profile"
	media = Media.query.get(current_user.id)
	return render_template("dashboard/dashboard_profile_page.html",title=title)