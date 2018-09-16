from flask import Flask, send_file, request, Response
from contours import get_contours

app = Flask(__name__)

@app.route("/")
def index():
	return "<h1>The Server is Up and Running!</h1>"

@app.route("/climb/api", methods=['GET', 'POST'])
def process():
	if request.method == 'GET':
		pass
	else:
		file = request.files['image'].read()
		print(file)
		return Response(file, mimetype='image/jpg')
			#pass image into classification function

