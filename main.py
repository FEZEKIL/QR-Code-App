import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create('Python is good!')
qr.png('qrcode.png', scale=8)

d=decode(Image.open('qrcode.png'))
print(d)