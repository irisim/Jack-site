import requests

url = 'http://127.0.0.1:5000/execute'
files = {'file': open('../images/about-img2.jpg', 'rb')}  # Replace with your image path

response = requests.post(url, files=files)

# Save the response content as an image
with open('flipped_image.jpg', 'wb') as f:
    f.write(response.content)

# Display the flipped image
from PIL import Image
flipped_image = Image.open('flipped_image.jpg')
flipped_image.show()
