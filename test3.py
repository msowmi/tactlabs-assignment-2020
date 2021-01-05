from flask import Flask, render_template,request
from werkzeug.utils import secure_filename
app = Flask(__name__)
import imgToExcel
@app.route("/")
@app.route("/choose")
def upload_file():
    
    return render_template('choose.html')
@app.route('/uploader',methods=['GET','POST'])

def upload_file():
    if request.method=='POST':
        f=request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
imgToExcel.conv()

if __name__=="__main__":
    app.run(debug = True)
