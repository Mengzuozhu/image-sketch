# -*- coding: UTF-8 -*-
import imageio

import sketch

FRAME_COUNT = 10
# second
DURATION = 0.5


def to_gif(in_image, rgb_out, out_file):
    images = []
    for i in range(FRAME_COUNT, 0, -1):
        images.append(sketch.merge(in_image, rgb_out, i / FRAME_COUNT))
    imageio.mimsave(out_file, images, duration=DURATION)


if __name__ == '__main__':
    file = 'demo.jpg'
    out = 'out/move_demo.gif'
    sketch.sketch_image(file, out, to_gif)
