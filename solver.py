from collections import deque
from utils import count_distance
from utils import manhattan_distance
import numpy as np
from test2 import linear_conflict_heuristic


def manhattan_heuristic(state, goal_state, number_of_tiles, size):
    distance = 0
    for i in range(number_of_tiles):
        if state[i] != goal_state[i] and state[i] != 0:
            ci = goal_state.index(state[i])
            y = (i // size) - (ci // size)
            x = (i % size) - (ci % size)
            distance += abs(y) + abs(x)

    return distance


def clone_and_swap(data, y0, y1):
    clone = list(data)
    tmp = clone[y0]
    clone[y0] = clone[y1]
    clone[y1] = tmp
    return tuple(clone)


def nextnodes(state, number_of_tiles, size, y):
    res = []

    if y % size > 0:
        left = clone_and_swap(state, y, y - 1)
        res.append((left, y - 1))
    if y % size + 1 < size:
        right = clone_and_swap(state, y, y + 1)
        res.append((right, y + 1))
    if y - size >= 0:
        up = clone_and_swap(state, y, y - size)
        res.append((up, y - size))
    if y + size < number_of_tiles:
        down = clone_and_swap(state, y, y + size)
        res.append((down, y + size))

    return res


def search(path, g, threshold, goal_state, number_of_tiles, size, y):
    state = path[0]
    f = g + manhattan_heuristic(state, goal_state, number_of_tiles, size)

    if f > threshold:
        return f
    if state == goal_state:
        return True

    minimum = float('inf')
    nodes = nextnodes(state, number_of_tiles, size, y)
    for node, zero in nodes:
        if node not in path:
            path.appendleft(node)
            tmp = search(path, g + 1, threshold, goal_state, number_of_tiles, size, zero)
            if tmp == True:
                return True
            if tmp < minimum:
                minimum = tmp
            path.popleft()

    return minimum


def solve(initial_state, goal_state, number_of_tiles, size):
    print(f'GOAL_STATE = {goal_state}')
    print(f'INITIAL STATE = {initial_state}')
    print()

    y = initial_state.index(0)
    threshold = manhattan_heuristic(initial_state, goal_state, number_of_tiles, size)
    path = deque([initial_state])

    while 1:
        tmp = search(path, 0, threshold, goal_state, number_of_tiles, size, y)
        if tmp == True:
            print(f"GOOD!")
            return path
        elif tmp == float('inf'):
            print(f"WRONG!")
            return False
        threshold = tmp
