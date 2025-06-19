from flask import Flask, request, redirect, url_for, send_file
import requests

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return redirect(request.url)
    
    file = request.files['image']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        # Save the file locally
        file.save('uploaded_image.jpg')
        
        """# Trigger the Google Colab script
        response = requests.post(
            'https://colab.example.com/execute', 
            files={'file': open('uploaded_image.jpg', 'rb')}
        )"""
        # Trigger the Google Colab script
        response = requests.post(
            'https://colab.research.google.com/drive/1GneERnizrm3h10Kc9awgTx3dE88oAC57', 
            files={'file': open('uploaded_image.jpg', 'rb')}
        )
        
        # Assuming the Colab script returns the processed image
        with open('processed_image.jpg', 'wb') as f:
            f.write(response.content)
        
        return send_file('processed_image.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)





