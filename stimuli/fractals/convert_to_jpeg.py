from PIL import Image

for i in range(111,112):
    type=str(int(i))
    for item in ['a', 'b','c']:
        name = type + item
        extensions = ['.png', '.jpg']
        print(name)
        im = Image.open("{0}{1}".format(name, extensions[0]))
        rgb_im = im.convert('RGB')
        rgb_im.save("{0}{1}".format(name, extensions[1]))