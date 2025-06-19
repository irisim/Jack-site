from flask import Flask, request, send_file, redirect, url_for
from PIL import Image
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return redirect('/')
    
    file = request.files['image']
    
    if file.filename == '':
        return redirect('/')
    
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        
        # Process the image
        image = Image.open(file_path)
        flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        
        # Save the processed image
        processed_file_path = os.path.join(PROCESSED_FOLDER, file.filename)
        flipped_image.save(processed_file_path)
        
        return redirect(url_for('processed_file', filename=file.filename))

@app.route('/processed/<filename>')
def processed_file(filename):
    return send_file(os.path.join(PROCESSED_FOLDER, filename), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
