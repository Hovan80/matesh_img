from PIL import Image
from matplotlib import pyplot

# img = Image.open("/imgs/img1.jpeg")
# img.paste( (255, 0, 0), (0, 0, 100, 100) )
# img.show()

# img = Image.open("/imgs/img1.jpeg")
# img.paste( (0, 128, 0), img.getbbox() )
# img.show()


# img = Image.open('/imgs/img1.jpeg')
# img2 = img.resize((200, 500))
# print(img2.size)
# img.paste((255, 0, 0), (9, 9, 211, 161))
# img.paste(img2, (10, 10))
# img.show()


# img = Image.open('/imgs/img1.jpeg')
# white = Image.new('RGB', (img.size[0], 100), (255, 255, 255))
# mask = Image.new('L', (img.size[0], 100), 64)
# img.paste(white, (0, 0), mask)
# img.show()


# img = Image.open('imgs/img1.jpeg')
# box = (100, 100, 400, 400)
# region = img.crop(box)
# region = region.transpose(Image.ROTATE_180)
# img.paste(region, box)
# img.show()


img = Image.open('./imgs/img1.jpeg')
pyplot.imshow(img)
print("Кликните три точки")
x = pyplot.ginput(3)
print('Вы кликнули:', x)



# img = Image.open('./imgs/img1.jpeg')
# pyplot.imshow(img)
# x = [100, 100, 400, 400]
# y = [200, 500, 200, 500]
# pyplot.plot(x, y, 'r*')
# pyplot.plot(x[:2], y[:2])
# pyplot.title('Plotting: img1.jpeg')
# pyplot.show()