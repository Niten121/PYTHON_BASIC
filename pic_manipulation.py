'''

Pillow and PIL cannot co-exist in the same environment . Before installing Pillow unonstall PIl
Pillow >1.0 no longer support "import Image".
please use "from PIL import Image "
Pillow >=2.1.0 no longer supports "import_imaging". please use "from PIL.Image core as_imaging"
'''

from PIL import Image


def resize_img(image_names, new_size=(200,200)):
    for img in image_names:
        demo_img = Image.open(image_names)
        demo_img = demo_img.resize(new_size)
        demo_img.save("resized"+image_names)
demo = 'demo.jpg'
resize_img(demo)
py_demo = demo.crop((100,100,50,50))
py_demo = demo.rotate(90)