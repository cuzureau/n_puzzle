from utils import count_distance
from utils import manhattan_distance
import numpy as np
import constant
import time
from test2 import linear_conflict_heuristic


def manhattan_heuristic(state):
    # tic = time.time()
    # print(f"MANHATTAN2")
    # print(f"--> STATE = {state}")

    distance = 0
    for i in range(constant.NUMBER_OF_TILES):
        if state[i] != 0 and state[i] != constant.GOAL_STATE[i]:
            ci = constant.GOAL_STATE.index(state[i])
            y = (i // constant.BOARD_LENGTH) - (ci // constant.BOARD_LENGTH)
            x = (i % constant.BOARD_LENGTH) - (ci % constant.BOARD_LENGTH)
            distance += abs(y) + abs(x)

    # print('MANHATTAN2', (time.time() - tic) * 1000)
    # exit()

    return distance


def nextnodes(state):
    res = []
    y = state.index(constant.EMPTY_TILE)

    print(y)
    exit()


def search(path, g, threshold):
    state = list(path.keys())[-1]
    f = g + manhattan_heuristic(state)

    if f > threshold:
        return f
    if state == constant.GOAL_STATE:
        return True

    minimum = float('inf')
    for n in nextnodes(state):
        if n not in path:
            path[n] = None
            tmp = search(path, g + 1, threshold)
            if tmp == True:
                return True
            if tmp < minimum:
                minimum = tmp
            path.popitem()

    return minimum


def solve(initial_state):
    print(f'GOAL_STATE = {constant.GOAL_STATE}')
    print(f'INITIAL STATE = {initial_state}')
    print()

    threshold = manhattan_heuristic(initial_state)
    # TODO check if deque is not faster
    path = {initial_state: None}

    while 1:
        tmp = search(path, 0, threshold)
        if tmp == True:
            print(f"GOOD!")
            return path.keys()
        elif tmp == float('inf'):
            print(f"WRONG!")
            return False
        threshold = tmp
