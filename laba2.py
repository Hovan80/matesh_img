from PIL import Image
import base64
from io import BytesIO

img = Image.open('./imgs/img1.jpeg')
img.show()

img_bin = Image.open('./imgs/img1.jpeg').convert('L')
img_bin.show()

with open('./imgs/img2.gif', 'rb') as f:
    img_object = Image.open(f)
    img_object.show()
    
with open('./imgs/img2.gif', 'rb') as f:
    img_string = base64.b64encode(f.read())
    print(img_string[:20], '...')
    
img_sio = BytesIO(base64.b64decode(img_string))
img = Image.open(img_sio)
img.show()