from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file", 400
    
    if file:
        # Open the image file
        image = Image.open(file.stream)
        
        # Flip the image left to right
        flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        
        # Save the flipped image to a BytesIO object
        img_io = io.BytesIO()
        flipped_image.save(img_io, 'JPEG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
