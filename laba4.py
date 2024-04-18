from PIL import Image
import matplotlib as plt

#///////////////////////////////////
# img = Image.open('./imgs/img1.jpeg')
# img.show()
# for x in range(img.size[0]):
#     for y in range(img.size[1]):
#         r, g, b = img.getpixel((x, y))
#         img.putpixel((x, y), (b, r, g))
# img.show()
#///////////////////////////////////
# img = Image.open('./imgs/img1.jpeg')
# r, g, b = img.split()

# img2 = Image.merge('RGB', (b, r, g))
# print(img2.mode)
# img2.show()
#///////////////////////////////////
img = Image.open('./imgs/img1.jpeg')
r, g, b = img.split()
plt.hist()