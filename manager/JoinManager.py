from PIL import Image

from handler import ImageJoinHanlder
from handler.sketch import SketchHandler

if __name__ == '__main__':
    file = '../in/demo.jpg'
    out = '../out/demoJoin.png'
    res = SketchHandler.sketch_image(file)
    raw = Image.open(file).transpose(Image.FLIP_LEFT_RIGHT)
    convert = Image.open(file).convert('L').transpose(Image.FLIP_LEFT_RIGHT)
    res = ImageJoinHanlder.join_multi([res, convert])
    res.save(out)
