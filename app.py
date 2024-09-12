from flask import Flask, request, render_template, send_file
from PIL import Image, ImageDraw, ImageFont
import io
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    color = request.form['color']
    img = Image.open(file.stream)

    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    text1 = "100% AI generated"
    text2 = "RealFakePhotos.com"

    # Coordinates for the text
    text1_position = (50, img.height - 150)
    text2_position = (50, img.height - 100)

    draw.text(text1_position, text1, fill=color, font=font)
    draw.text(text2_position, text2, fill=color, font=font)

    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
