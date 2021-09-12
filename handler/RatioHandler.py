from PIL import Image

# 原始图片比例
RAW_X_RANGE = [0, 0]
RAW_Y_RANGE = [0, 1]


def process(raw_image: Image.Image, out_image: Image.Image):
    """
    比例处理
    :param raw_image:
    :param out_image:
    :return:
    """
    x_begin = int(raw_image.width * RAW_X_RANGE[0])
    x_end = int(raw_image.width * RAW_X_RANGE[1])
    y_begin = int(raw_image.height * RAW_Y_RANGE[0])
    y_end = int(raw_image.height * RAW_Y_RANGE[1])
    for x in range(x_begin, x_end):
        for y in range(y_begin, y_end):
            raw_pixel = raw_image.getpixel((x, y))
            out_image.putpixel((x, y), raw_pixel)
    return out_image
