# -*- coding: UTF-8 -*-
import cv2
import imageio
from PIL import Image

import sketchOpenCv

FRAME_COUNT = 15
# second
DURATION = 0.3


def to_gif(in_image, rgb_out, out_file):
    images = []
    for i in range(FRAME_COUNT, 0, -1):
        merge = sketchOpenCv.merge(in_image, rgb_out, raw_width_ratio=i / FRAME_COUNT)
        image = Image.fromarray(cv2.cvtColor(merge, cv2.COLOR_BGR2RGB))
        images.append(image)
    imageio.mimsave(out_file, images, duration=DURATION, subrectangles=True)


if __name__ == '__main__':
    file = 'demo.jpg'
    out = 'out/move_demo.gif'
    sketchOpenCv.sketch_image(file, out, to_gif)
