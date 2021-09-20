from PIL import Image


def join_by_path(png1, png2):
    """
    :param png1: path
    :param png2: path
    :return: Image.Image
    """
    return join_multi([Image.open(png1), Image.open(png2)])


def join(img1: Image.Image, img2: Image.Image):
    """
    横向拼接图片
    :param img1:
    :param img2:
    :return:
    """
    return join_multi([img1, img2])


def join_multi(images: [Image.Image]):
    """
    横向拼接图片
    :param images:
    :return:
    """
    img1 = images[0]
    size1 = img1.size
    joint = Image.new('RGB', (size1[0] * len(images), size1[1]))
    joint.paste(img1, (0, 0))
    for i in range(1, len(images)):
        img = images[i]
        img = img.resize(size1, Image.ANTIALIAS)
        joint.paste(img, (size1[0] * i, 0))
    return joint


if __name__ == '__main__':
    file = '../in/demo.jpg'
    out = '../out/demoJoin.png'
    res = join_by_path(file, file)
    res.save(out)
