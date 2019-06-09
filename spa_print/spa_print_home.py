from spa_print import spa_print
from flask_login import current_user, login_required
from flask import render_template, jsonify

@spa_print.route('/', defaults={'path': ''})
@spa_print.route('/<path:path>')
def catch_all(path):
    return render_template("spa_print/index.html")
	
	

