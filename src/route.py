from app import *

@app.route("/", methods=["GET"])
def index():
	"""
	If the user does a GET /, then we will render index.html for them. This
	effectively serves the user the front-end.
	"""

	return render_template("index.html")

