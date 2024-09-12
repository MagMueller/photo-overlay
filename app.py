from flask import Flask, render_template, request, send_file
from PIL import Image
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        # Save the uploaded file
        file_path = os.path.join('static/images', file.filename)
        file.save(file_path)

        # Open the uploaded image and the template image
        uploaded_image = Image.open(file_path).convert("RGBA")
        template_image = Image.open('static/images/Template.png').convert("RGBA")

        # Ensure both images are the same size
        uploaded_image = uploaded_image.resize(template_image.size)

        # Composite the images
        result_image = Image.alpha_composite(uploaded_image, template_image)

        # Save the result
        result_path = os.path.join('static/images', 'result.png')
        result_image.save(result_path)

        return render_template('result.html', result_image='static/images/result.png')


@app.route('/download')
def download():
    return send_file('static/images/result.png', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
