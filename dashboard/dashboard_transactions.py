from flask import render_template, redirect, url_for, request
from dashboard import dashboard_print

@dashboard_print.route("/transactions")
def dashboard_transactions_view():
	title = "Transactions"
	return render_template("dashboard/dashboard_transactions_page.html",title=title)