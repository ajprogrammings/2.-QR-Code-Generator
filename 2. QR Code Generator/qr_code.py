import qrcode as qr
img = qr.make("https://www.youtube.com/channel/UC4dB-S8qnZ3gikV8rFSgLTQ")
img.save("ajprogrammings_youtube.png")