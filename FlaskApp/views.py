import os
import excel
from flask import Flask, render_template, request, redirect, url_for, send_file, flash
from werkzeug import secure_filename
from FlaskApp import app

UPLOAD_FOLDER = '/var/www/FlaskApp/FlaskApp/uploads'
ALLOWED_EXTENSIONS = set(['txt','pdf','png','jpg','jpeg','gif','xlsx'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/state-reporter')
def upload():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        vendors = request.files['vendors']
        if vendors.filename== '':
            return send_file(os.path.join(app.config['UPLOAD_FOLDER'], 'novendors.txt'))
        if file.filename == '':
            flash('No selected file')
            return send_file(os.path.join(app.config['UPLOAD_FOLDER'], 'novendors.txt'))
        if file and vendors:
            vendor_filename = secure_filename(vendors.filename)
            filename = secure_filename(file.filename)
            vendors.save(os.path.join(app.config['UPLOAD_FOLDER'], vendor_filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            excel.main(os.path.join(app.config['UPLOAD_FOLDER'], filename), os.path.join(app.config['UPLOAD_FOLDER'], vendor_filename))
            return send_file('/var/www/FlaskApp/FlaskApp/export.xlsx', attachment_filename='export.xlsx')
    return redirect(request.url)

