import qrcode

data = "https://www.linkedin.com/in/himanshu-heda/"

qr = qrcode.make(data)
qr.save("linkedin.png")

print("QR Code Generated Successfully!")