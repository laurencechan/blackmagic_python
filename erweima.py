# coding=utf-8

import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('hello,laurencechan')
qr.make(fit=True)
img = qr.make_image()
img.save('123.png')

if __name__ == '__main__':
    pass
