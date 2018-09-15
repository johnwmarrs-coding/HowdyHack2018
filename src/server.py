from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return "<h1>The Server is Up and Running!</h1>"

@app.route("/climb/api", methods=['GET', 'POST'])
def process():
	if request.method == 'GET':
		pass
	else:
		pass

