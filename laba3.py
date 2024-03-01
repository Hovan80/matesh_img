from PIL import Image

# img = Image.open('imgs/img1.jpeg')
# print(img.mode)
# obj = img.load()
# print(obj[25, 45])
# obj[25, 45] = (255, 0, 0)
# img.show()

# print(img.getpixel((25, 45)))
# img.putpixel(
#     (25, 45), (0, 255, 0)
# )
# img.show()

#////////////////////////////////////////

# img = Image.open('imgs/img1.jpeg')
# print(img.mode)
# r, g, b = img.split()
# mask = Image.new('L', img.size, 128)
# img = Image.merge('RGBA', (r, g, b, mask))
# print(img.mode)
# img.show()

#////////////////////////////////////////

# img = Image.open('imgs/img1.jpeg')
# print(img.mode)
# img2 = img.convert('RGBA')
# print(img2.mode)
# img2.show()

# img2 = img.convert('P', None, Image.FLOYDSTEINBERG, Image.ADAPTIVE, 128)
# print(img2.mode)
# img2.show()

# img.save('imgs/tmp.jpeg')
# img.save('imgs/tmp.bmp', 'BMP')

# file = open('imgs/tmp2.bmp', 'wb')
# img.save(file, "BMP")
# file.close()

#////////////////////////////////////////

