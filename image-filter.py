from PIL import Image, ImageFilter

image = Image.open(r"image2.jpg")

image2 = image.filter(ImageFilter.UnsharpMask)

image.show()
image2.show()

