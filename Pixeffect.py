import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

import json
def callit(roi,img,filter):
	from beginStyling import Style
	Style(roi,img,filter)
app = Flask(__name__)

@app.route("/")
@app.route("/upload")
def upload():
	return render_template('upload.html')
@app.route("/index1")
def index1():
	return render_template('index1.html')

@app.route("/upload2",methods=['POST','GET'])
def upload_file():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'photos' not in request.files:
			flash('No file part')
			return render_template(upload.html,error = "Please upload a file")
		file = request.files['photos']
		# if user does not select file, browser also
		# submit an empty part without filename
		if file.filename == '':
			flash('No selected file')
			return render_template(upload.html,error = "Error File not found, please try again.")
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join('static/uploads/'+str(file.filename)))
			print(request.form['choice'])
			callit(img = 'static/uploads/'+str(file.filename) ,filter = request.form['filter'],roi=request.form["choice"])
			return render_template('preview.html',original = 'uploads/'+str(filename),newimg = 'images/style'+str(filename))
		else:
			return render_template(upload.html,error = "Error while storing file, Please try again")
if __name__ == "__main__":
	app.secret_key = os.urandom(24)
	app.run(host = "0.0.0.0", port=5000, debug =True)
