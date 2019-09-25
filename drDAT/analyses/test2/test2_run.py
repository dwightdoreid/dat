import os
from flask import Flask, render_template, request
# from werkzeug import secure_filename

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'C:\\Users\\Dwight\\Documents\\Projects\\Dat\\Dev3\\dataFiles'
app.config['UPLOAD_FOLDER'] = 'dataFiles'

@app.route('/test2_hello', methods = ['POST', 'GET'])
def test2_hello():
    if request.method == 'POST':
        f = request.files['myFile']
        # f.save(secure_filename(f.filename))
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        
        return "<h2>file uploaded successfully</h2>"
        # result = request.form
        # return result
    return "<h1>Hello from test 2</h1>"

if __name__ == '__main__':
    app.run(debug = True, port = 5500)