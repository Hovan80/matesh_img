from PIL import Image, ImageFilter

# img = Image.open('./imgs/img1.jpeg')
# img2 = img.filter(ImageFilter.BLUR)
# img2.show()


img = Image.open('./imgs/img1.jpeg').convert('L')
img = img.filter(ImageFilter.CONTOUR)
img.show()