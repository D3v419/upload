from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Konfigurasi folder upload
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Pastikan folder upload ada
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "Tidak ada file yang diunggah", 400

    file = request.files['file']

    if file.filename == '':
        return "Nama file kosong", 400

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return f"File {file.filename} berhasil diunggah ke {file_path}"

if __name__ == '__main__':
       app.run(host='0.0.0.0', port=443, debug=True)
