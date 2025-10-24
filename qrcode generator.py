# QR Code Generator for Instagram URL

import qrcode as qr

data=input("Enter the Instagram URL to generate QR code: ")
img=qr.make(data)
img.save("instagram_qr.png")
img.show()
print("Qr code generated successfully and saved as instagram_qr.png")

#Qr code using object oriented programming


import qrcode

class qrcode_generator:
    def __init__(self,data,filename):
        self.data=data
        self.filename=filename
    def generate_qr(self):
        img=qrcode.make(self.data)
        img.save(self.filename)
        img.show()
        print("Qr code generated successfully and saved as",self.filename)

data=input("Enter the URL to generate QR code: ")
filename=input("Enter the filename to save the QR code with extension (e.g., .png , .jpg): ")
qr_gen=qrcode_generator(data,filename)
qr_gen.generate_qr()


#now using more customization 


import qrcode 
from PIL import Image

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=15,
    border=4,
)
data=input("Enter your URL fo which you wanna make customized QR code: ")
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="red", back_color="blue")
img.save("custom_instagram_qr.png")
img.show()
print("Customized Qr code generated successfully and saved as custom_instagram_qr.png")