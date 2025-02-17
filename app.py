from flask import Flask, request, send_file, render_template
import qrcode
import os

app = Flask(__name__)

# Folder to store QR codes
QR_FOLDER = "static/qrcodes"
os.makedirs(QR_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        if not url:
            return "Please provide a valid URL.", 400

        # Generate QR code
        qr = qrcode.make(url)
        qr_path = os.path.join(QR_FOLDER, "qrcode.png")
        qr.save(qr_path)

        return render_template("index.html", qr_code=qr_path)

    return render_template("index.html", qr_code=None)

@app.route("/download")
def download_qr():
    qr_path = os.path.join(QR_FOLDER, "qrcode.png")
    return send_file(qr_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
