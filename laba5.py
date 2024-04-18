from PIL import Image

# img = Image.open('./imgs/img1.jpeg')
# img2 = img.copy()
# img2.show()


# img = Image.open('./imgs/img2.gif')
# print(img.size)
# img.thumbnail((400, 300), Image.BILINEAR)
# print(img.size)
# img.thumbnail((400, 100), Image.BILINEAR)
# print(img.size)


# img = Image.open('./imgs/img1.jpeg')
# print(img.size)
# img.show()
# newsize = (400, 400)
# imgnr = img.resize(newsize)
# img.show()


# img = Image.open('/imgs/img1.jpeg')
# img2 = img.crop([0, 0, 100, 100])
# img2.load()
# print(img2.size)


# img = Image.open('./imgs/img1.jpeg')
# print(img.size)
# img.show()
# box = (100, 100, 300, 300)
# img2 = img.crop(box)
# newsize = (400, 400)
# img2nr = img2.resize(newsize)
# img2nr.show()


img = Image.open("/imgs/img1.jpeg")
# print(img.size)
# img2 = img.rotate(90)
# print(img2.size)
# img3 = img.rotate(45, Image.NEAREST)
# print(img3.size)
# img4 = img.rotate(45, expand=True)
# print(img4.size)

img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
img2.show()
img3 = img.transpose(Image.FLIP_TOP_BOTTOM)
img3.show()
img4 = img.transpose(Image.ROTATE_90)
img4.show()
img5 = img.transpose(Image.ROTATE_180)
img5.show()
