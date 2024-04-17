# ==================================================================================================================================================================== #
# INSTALL ALL LIBRARIES
# CREATE A FUNCTION THAT COLECT A TEXT AND CONVERT IT TO A QR CODE
# SAVE THE QR CODE AS A IMAGEM 
# RUN THE FUNCTION CREATED
# ==================================================================================================================================================================== #

import qrcode

darkBlue = '#0815a6'

def generate_qrcode(text):
    
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(text)
    qr.make_image(fit=True)
    img = qr.make_image(fill_color="black", back_color="darkBlue")
    img.save("qrimg.png")


url = input("Enter you URL: ")
generate_qrcode(url)