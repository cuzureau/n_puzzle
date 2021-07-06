import argparse
from heuristics import heuristics
import numpy as np
import re



def generate_state():
    size = 3
    arr = np.arange(size * size)
    arr2 = np.random.permutation(arr)

    return size, tuple(arr2)


def get_data_from_file(file):
    data = file.read().splitlines()
    file.close()

    data = [line.strip().split('#')[0] for line in data]    # delete comments lines
    data = [line for line in data if len(line) > 0]         # delete empty lines

    return data


def data_is_valid(data):
    sizes = re.findall('[0-9]+', data[0])

    if len(sizes) == 1:
        size = int(sizes[0])
    else:
        return False
    if size != len(data[1:]):
        return False
    for line in data[1:]:
        numbers = re.findall('[0-9]+', line)
        if size != len(numbers):
            return False

    return True


def parser():
    p = argparse.ArgumentParser(description='n-puzzle by @cuzureau')
    p.add_argument('-heur', help='heuristic function', choices=list(heuristics.keys()), default='manhattan')
    p.add_argument('file', help='input file', nargs='?', type=argparse.FileType('r'))
    args = p.parse_args()

    if not args.file:
        size, initial_state = generate_state()
    else:
        data = get_data_from_file(args.file)
        print(f'Puzzle initial state is {"valid" if data_is_valid(data) else "invalid"}')
        exit()

        # size, initial_state = define_state(args.file)

    return initial_state, size, args.heur



