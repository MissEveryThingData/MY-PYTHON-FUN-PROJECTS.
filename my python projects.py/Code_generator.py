import qrcode

def generate_qrcode(text):
    qr = qrcode.QRcode(
        version = 1,
        error_correction = qrcode.constants.ERROR_correct,
        box_size = 10,
        border = 4,
        )
    qr.add_add(text)
    qr.make (fit = True)
    img = qr.make_image(fill_color = "black",background_color = "white" )
    img.save('qrimg001.png')

    url = input ("Enter your url:")
    generate_qrcode(url)