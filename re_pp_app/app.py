from flask import *
from pickle import *
import os

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
	if request.method == "POST":
		fn ="re.pkl"
		if os.path.exists(fn):
			f = open(fn, "rb")
			model = load(f)
			f.close()
			area = float(request.form["area"])
			bedrooms = float(request.form["bedrooms"])
			price = model.predict([[area, bedrooms]])
			msg = "price= "+ str(round(price[0], 2)) + "crs"
			return render_template("home.html", msg=msg)
		else:
			print(fn, "does not exists")
	else:
		return render_template("home.html")

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)