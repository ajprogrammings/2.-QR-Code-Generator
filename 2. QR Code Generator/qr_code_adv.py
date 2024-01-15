import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=4,)
qr.add_data("https://www.youtube.com/channel/UC4dB-S8qnZ3gikV8rFSgLTQ")
qr.make(fit=True)
img=qr.make_image(fill_color="red")
img.save("ajprogrammings.png")