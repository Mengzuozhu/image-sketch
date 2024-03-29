# -*- coding: UTF-8 -*-
import cv2
import imageio
from PIL import Image

from handler.sketch import SketchOpenCv

FRAME_COUNT = 15
# second
DURATION = 0.3


def to_gif(in_image, rgb_out, out_file):
    images = []
    for i in range(FRAME_COUNT, 0, -1):
        merge = SketchOpenCv.merge(in_image, rgb_out, raw_width_ratio=i / FRAME_COUNT)
        image = Image.fromarray(cv2.cvtColor(merge, cv2.COLOR_BGR2RGB))
        images.append(image)
    imageio.mimsave(out_file, images, duration=DURATION, subrectangles=True)


if __name__ == '__main__':
    file = '../../in/demo.jpg'
    out = '../../out/move_2.gif'
    SketchOpenCv.sketch_image(file, out, to_gif)
