from flask import Flask , request, render_template
from werkzeug.utils import secure_filename
import os 
import app_helper


app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route('/uploader', methods=['POST'])
def upload_file():
    predictions=''
    if request.method =='POST':
        f= request.files['file']
        
        basepath =os.path.dirname(__file__)
        file_path=os.path.join(basepath, 'static', 'uploads', secure_filename(f.filename))
        f.save(file_path)
        
        predictions =app_helper.p(file_path)
        print(predictions)
        
    return render_template('upload.html',predictions=predictions, display_image=f.filename)

if __name__ =='__main__':
    app.run(debug=True, port =8000)
