#home page 
from flask import render_template
from account import account_print


	


	
#@account_print.route("/accounts/forgot-password")
@account_print.route("/forgot-password")
def forgot_password_view():
	title = "Forgot Password"
	return render_template("accounts/forgot_password_page.html",title=title)
