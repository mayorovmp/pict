import numpy as np
from PIL import Image
import os


class Tile:
    def __init__(self):
        _left = _right = _top = _down = None


directory = 'result' + os.sep
_RED = (255, 0, 0)
path = 'data/1200.png'
SIZE = 512
BLOCK_SIZE = 64
_img_map = Image.open(path)
_pixels = _img_map.load()


def cord_by_num(n):
    """Return (x, y) coords."""
    row_size = SIZE // BLOCK_SIZE
    return BLOCK_SIZE * (n % row_size), BLOCK_SIZE * (n // row_size)


def mark(n):
    x, y = cord_by_num(n)
    for i in range(BLOCK_SIZE):
        for j in range(BLOCK_SIZE):
            _pixels[x + i, y + j] = _RED


def swap(n1, n2):
    x1, y1 = cord_by_num(n1)
    x2, y2 = cord_by_num(n2)
    for i in range(BLOCK_SIZE):
        for j in range(BLOCK_SIZE):
            t = _pixels[x1 + i, y1 + j]
            _pixels[x1 + i, y1 + j] = _pixels[x2 + i, y2 + j]
            _pixels[x2 + i, y2 + j] = t


def get_distance_r_l(n1, n2):
    """Distance btw n1 and n2 by right side of n1 and left side of n2 """
    distance = 0
    x1, y1 = cord_by_num(n1)
    x2, y2 = cord_by_num(n2)
    for i in range(BLOCK_SIZE):
        distance += abs(_pixels[x1 + BLOCK_SIZE - 1, y1 + i][0] - _pixels[x2, y2 + i][0])
        distance += abs(_pixels[x1 + BLOCK_SIZE - 1, y1 + i][1] - _pixels[x2, y2 + i][1])
        distance += abs(_pixels[x1 + BLOCK_SIZE - 1, y1 + i][2] - _pixels[x2, y2 + i][2])
    return distance


def run():
    mem = {}
    for i in range(63):
        mem[i] = get_distance_r_l(0, i)
    l = sorted(mem.items(), key=lambda p: p[1])
    for key in l:
        print(str(key[0]) + '  '+ str(key[1]))


    # states = np.array(_img_map)
    _img_map.save(directory + "{0}.png".format('a'))
    print('hello')


run()
