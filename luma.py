# luma.py


import sys
from math import sqrt
from dataclasses import dataclass


@dataclass
class Pixel:
    r: float
    g: float
    b: float

def luma1(r: int, g: int, b: int) -> float:
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def luma2(r: int, g: int, b: int) -> float:
    return 0.299 * r + 0.587 * g + 0.114 * b

def luma3(r: int, g: int, b: int) -> float:
    return sqrt(0.299 * r ** 2 + 0.587 * g ** 2 + 0.114 * b ** 2)

def luma4(r: int, g: int, b: int, l=luma1) -> float:
    # from less.js color class luma definition
    def helper(color):
        return 12.92 if color <= 0.03928 else pow(((color + 0.055) / 1.055), 2.4)
    return int(l(helper(r/255), helper(g/255), helper(b/255)) * 100)

luma = [ luma1, luma2, luma3, luma4 ]

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 3:
        raise Exception("Not enough values to calculate luma")
    elif len(args) > 4:
        raise Exception("Too many values to calculate luma")
    if len(args) == 4:
        standard = int(args[0])
        if not 0 <= standard <= len(luma) - 1:
            raise Exception("Argument for standard function is out of range")
        r, g, b = args[1:]
    else:
        standard = 0
        r, g, b = args

    print(luma[standard](int(r), int(g), int(b)))

