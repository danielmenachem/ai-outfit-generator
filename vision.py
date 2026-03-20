from PIL import Image

def detect_dominant_color(image_path):
    image = Image.open(image_path)
    image = image.convert("RGB")
    image = image.resize((100, 100))

    pixels = list(image.getdata())

    total_r = 0
    total_g = 0
    total_b = 0

    for r, g, b in pixels:
        total_r += r
        total_g += g
        total_b += b

    num_pixels = len(pixels)

    avg_r = total_r / num_pixels
    avg_g = total_g / num_pixels
    avg_b = total_b / num_pixels

    if avg_r > avg_g and avg_r > avg_b:
        return "red"
    elif avg_g > avg_r and avg_g > avg_b:
        return "green"
    elif avg_b > avg_r and avg_b > avg_g:
        return "blue"
    elif avg_r > 180 and avg_g > 180 and avg_b > 180:
        return "white / light"
    elif avg_r < 80 and avg_g < 80 and avg_b < 80:
        return "black / dark"
    else:
        return "neutral"
    