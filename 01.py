from itertools import product
import numpy as np


def part1(data):
    __import__('time').sleep(1)
    # Data is automatically read from 01.txt
    data = np.fromstring(data, dtype=int, sep='\n')
    return [x * y for x, y in product(data, data) if x + y == 2020][0]


def part2(data):
    __import__('time').sleep(1)
    # Data is automatically read from 01.txt
    data = np.fromstring(data, dtype=int, sep='\n')
    return [x * y * z for x, y, z in product(data, data, data) if x + y + z == 2020][0]
