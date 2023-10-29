import random

def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def hex2rgb(hexcode):
    return tuple(map(ord, hexcode[1:].decode('hex')))


def random_color_string(string):
    local_map = []
    for letter in string:
        color = rgb2hex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        local_map.append((letter, color))
    return local_map


def random_color_rgb():
    col = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    return col