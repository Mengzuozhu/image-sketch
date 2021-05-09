from PIL import Image

X_INTERVAL = 50
Y_INTERVAL = 0
WIDTH = 10


def stripe(raw_image: Image.Image, out_image: Image.Image):
    """
    条纹处理
    :param raw_image:
    :param out_image:
    :return:
    """
    x_ranges = get_ranges(raw_image.width, X_INTERVAL, WIDTH)
    y_ranges = get_ranges(raw_image.height, Y_INTERVAL, WIDTH)

    for x in range(0, raw_image.width):
        if x_ranges and x not in x_ranges:
            continue
        for y in range(0, raw_image.height):
            if y_ranges and y not in y_ranges:
                continue
            raw_pixel = raw_image.getpixel((x, y))
            out_image.putpixel((x, y), raw_pixel)
    return out_image


def get_ranges(end, interval, width):
    x_ranges: set = set()
    if interval == 0:
        return x_ranges
    for x in range(0, int(end / interval)):
        num = x * interval
        for i in range(num, num + width):
            x_ranges.add(i)
    return x_ranges
