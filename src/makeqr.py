import qrcode
import zbarlight
import numpy as np
from PIL import Image


def boolToInt(array):
    return np.where(array == True, 255, 0)

def generateQrcode(data, version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=5, border=4):
    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data=data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    return boolToInt(np.array(img))

def decodeQrcode(data):
    codes = zbarlight.scan_codes('qrcode', Image.fromarray(np.uint8(data)))
    for i in codes:
        codes = i.decode('utf-8', 'ignore')

    return codes

def qrsizeChange(array):
    next_pow2 =  int(np.log2(2 ** np.ceil(np.log2(len(array)))))
    return np.asarray(Image.fromarray(np.uint8(array)).resize((int(2**next_pow2), int(2**next_pow2))))