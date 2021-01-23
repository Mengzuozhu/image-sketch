# -*- coding: UTF-8 -*-
import time

import cv2

SCALE = 255
# 必须为正奇数
KSIZE_FOR_SHADOW = 31
# 原始图片比例
RAW_WIDTH_RATIO = 0.5
RAW_HEIGHT_RATIO = 1


def sketch_image(in_file, out_file):
    """
    素描图片
    :param in_file:
    :param out_file:
    """
    in_image = cv2.imread(in_file)
    gray_image = cv2.cvtColor(in_image, cv2.COLOR_RGB2GRAY)
    blur_image = cv2.GaussianBlur(gray_image, ksize=(KSIZE_FOR_SHADOW, KSIZE_FOR_SHADOW), sigmaX=0, sigmaY=0)
    out_image = cv2.divide(gray_image, blur_image, scale=SCALE)
    rgb_out = cv2.cvtColor(out_image, cv2.COLOR_GRAY2RGB)
    merge_out = merge(in_image, rgb_out)
    cv2.imwrite(out_file, merge_out)


def merge(raw_image, gray_image, raw_width_ratio=RAW_WIDTH_RATIO, raw_height_ratio=RAW_HEIGHT_RATIO):
    out_image = gray_image.copy()
    height, width = out_image.shape[:2]
    x_begin = 0
    x_end = int(width * raw_width_ratio)
    y_begin = 0
    y_end = int(height * raw_height_ratio)
    for x in range(x_begin, x_end):
        for y in range(y_begin, y_end):
            out_image[y, x] = raw_image[y, x]
    return out_image


def sketch_cv(in_file, out_file):
    in_image = cv2.imread(in_file)
    gray_image = cv2.cvtColor(in_image, cv2.COLOR_RGB2GRAY)
    blur_image = cv2.GaussianBlur(gray_image, ksize=(KSIZE_FOR_SHADOW, KSIZE_FOR_SHADOW), sigmaX=0, sigmaY=0)
    out_image = cv2.divide(gray_image, blur_image, scale=SCALE)
    cv2.imwrite(out_file, out_image)


if __name__ == '__main__':
    file = 'demo.jpg'
    out = 'out/demo.jpg'
    start = time.time()
    sketch_image(file, out)
    print(time.time() - start)
