from PIL import Image,ImageFilter,ImageEnhance
img = Image.open('demo.jpg')

grey = img.convert('L')
edge = img.filter(ImageFilter.FIND_EDGES)
contrast = ImageEnhance.Contrast(img).enhance(1.5)
bright = ImageEnhance.Brightness(img).enhance(1.2)

img.show()
grey.show()
edge.show()
contrast.show()
bright.show()