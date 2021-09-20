from PIL import Image, ImageFilter, ImageOps


def process(image: Image.Image):
    for i in range(1):
        image = image.filter(ImageFilter.BLUR)
    return image


if __name__ == '__main__':
    file = '../in/demo.jpg'
    out = '../out/demof.png'
    img = Image.open(file).convert('L')
    img = ImageOps.invert(img)
    res = process(img).convert("RGB")
    res.save(out)
