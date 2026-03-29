from flask import Flask, render_template, request, send_file, send_from_directory
import qrcode
import os
import uuid

app = Flask(__name__)

QR_FOLDER = "qr_codes"
if not os.path.exists(QR_FOLDER):
    os.makedirs(QR_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_file = None

    if request.method == 'POST':
        url = request.form.get('url')

        if url:
            filename = f"{uuid.uuid4().hex}.png"
            file_path = os.path.join(QR_FOLDER, filename)

            img = qrcode.make(url)
            img.save(file_path)

            qr_file = filename

    return render_template('index.html', qr_file=qr_file)


@app.route('/qr_codes/<filename>')
def serve_qr(filename):
    return send_from_directory(QR_FOLDER, filename)


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(QR_FOLDER, filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)