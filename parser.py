import argparse
from heuristics import heuristics
import numpy as np


def generate_board(size):
    arr = np.arange(size * size)
    arr2 = np.random.permutation(arr)

    return tuple(arr2)


def is_input():
    parser = argparse.ArgumentParser(description='n-puzzle by @cuzureau')
    parser.add_argument('heuristic', action='store_true', help='heuristic function', default='manhattan')
    parser.add_argument('file', nargs='?', help='input file', type=argparse.FileType('r'))

    args = parser.parse_args()

    if not args.file:
        return False
    else:
        data = args.file.read().splitlines()
        args.file.close()
        return data, args
