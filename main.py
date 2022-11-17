from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from modeler.pdfaudio import extract_text, speaks
from flask import send_from_directory
import base64
# app 

app = Flask(__name__)

# app.config["UPLOAD_FOLDER"] = "./books/"
app.config["UPLOAD_FOLDER"] = "/tmp/"

@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/display', methods = ['GET','POST'])
def display_file():
    if request.method== 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        books= app.config['UPLOAD_FOLDER'] + filename
        f.save(books)
        file = open(books,"rb")
        mytext = extract_text(file)
        audio= speaks(mytext)
        encoded = base64.b64encode(audio)
        #books= send_from_directory("books", filename)
        print(books)
    return render_template('intento.html', value= encoded, books=filename)

@app.route('/send_doc/<filename>')
def send_doc(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == '__main__':
    app.run()
