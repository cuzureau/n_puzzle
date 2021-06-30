from collections import deque
from utils import count_distance
from utils import manhattan_distance
import numpy as np
from test2 import linear_conflict_heuristic


def clone_and_swap(data, y0, y1):
    clone = list(data)
    tmp = clone[y0]
    clone[y0] = clone[y1]
    clone[y1] = tmp

    return tuple(clone)


def nextnodes(state, number_of_tiles, size):
    res = []
    y = state.index(0)

    if y % size > 0:
        left = clone_and_swap(state, y, y - 1)
        res.append(left)
    if y % size + 1 < size:
        right = clone_and_swap(state, y, y + 1)
        res.append(right)
    if y - size >= 0:
        up = clone_and_swap(state, y, y - size)
        res.append(up)
    if y + size < number_of_tiles:
        down = clone_and_swap(state, y, y + size)
        res.append(down)

    return res


def search(heuristic, path, g, threshold, goal_state, number_of_tiles, size, node_count):
    state = path[0]
    f = g + heuristic(state, goal_state, number_of_tiles, size)
    node_count += 1

    if f > threshold:
        return f, node_count
    if state == goal_state:
        return True, node_count

    minimum = float('inf')
    nodes = nextnodes(state, number_of_tiles, size)

    for node in nodes:
        if node not in path:
            path.appendleft(node)
            tmp, node_count = search(heuristic, path, g + 1, threshold, goal_state, number_of_tiles, size, node_count)
            if tmp == True:
                return True, node_count
            if tmp < minimum:
                minimum = tmp
            path.popleft()

    return minimum, node_count


def solve(heuristic, initial_state, goal_state, number_of_tiles, size):

    threshold = heuristic(initial_state, goal_state, number_of_tiles, size)
    path = deque([initial_state])
    node_count = 0

    while 1:
        tmp, node_count = search(heuristic, path, 0, threshold, goal_state, number_of_tiles, size, node_count)
        if tmp == True:
            print(f"GOOD!")
            return path, node_count
        elif tmp == float('inf'):
            print(f"WRONG!")
            return False, node_count
        threshold = tmp
