from PIL import Image

demo = Image.open('demo.jpg')
w , h = demo.size
for x in range(w):
    for y in range(h):
        pix_cod = (x,y)
        r,g,b = demo.getpixel(pix_cod)

        neg_color = (255-r,255-g,255,b)
        demo.putpixel(pix_cod,neg_color)
demo.show()