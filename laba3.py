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

# img = Image.new("RGB", (100, 100))
# img.show() # Черный квадрат

# img = Image.new("RGB", (100, 100), (255, 0, 0))
# img.show() # Красный квадрат

# img = Image.new("RGB", (100, 100), "green")
# img.show() # Зеленый квадрат

# img = Image.new("RGB", (100, 100), "#f00")
# img.show() # тоже красный квадрат

# img = Image.new("RGB", (100, 100), "white")
# img.show() # Белый квадрат

# img = Image.new("RGB", (320, 240), "silver")
# img.show() # Серый квадрат

# img = Image.new("RGB", (320, 240), "rgb(205,100,200)")
# img.show() # цветной прямоугольник

# img = Image.new("RGB", (320, 240), "rgb(10%,100%,40%)")
# img.show() # цветной прямоугольник. Каналы в процентах

# img = Image.new("RGB", (640, 480), "rgb(205,100,200)")
# img.show() # сиреневый прямоугольник 

# for x in range(640):
#  for y in range(480):
#     img.putpixel((x,y),(0,160,0))
# img.save("okno.png", "PNG")
# img.show() # зеленый прямоугольник

img = Image.new("RGB", (640, 480), "rgb(205,100,200)")
img.show() # сиреневый прямоугольник

for x in range(640):
    for y in range(480):
        img.putpixel((x,y), (int(x/3), int((x+y)/6), int(y/3)))
img.save("okno.png", "PNG")
img.show() # прямоугольник с функциональной раскраской