from PIL import Image

from handler import ImageJoinHanlder
from handler.sketch import SketchHandler

if __name__ == '__main__':
    file = '../in/demo.jpg'
    out = '../out/demoJoin.png'
    res = SketchHandler.sketch_image(file)
    res = ImageJoinHanlder.join_multi([res, Image.open(file).convert('L'), Image.open(file)])
    res.save(out)
