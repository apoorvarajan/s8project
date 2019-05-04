from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
import os
import cv2
import model_predict
UPLOAD_FOLDER = os.path.join('static', 'img')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def upload_file():
   return render_template('page1.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename("picture.png")))
   return redirect(url_for('upload_file'))
@app.route('/col' , methods=['GET', 'POST'])
def color():
   img=cv2.imread(os.path.join('static','img',secure_filename("picture.png")))
   model_predict.model_predict(img)
   return redirect(url_for('upload_file'))

	
if __name__ == '__main__':
   app.run(debug = True)