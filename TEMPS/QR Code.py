import qrcode

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_M,
    box_size = 10,
    border = 1
)

qr.add_data("@djoleeradovic")
qr.make(fit= True)

graph = qr.make_image(fill_color = "blue", back_color = "white")
graph.save("qrcode.jpeg")