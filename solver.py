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


def count_conflicts(row, goal_row):
    conflicts = 0

    for i, (tile, goal_tile) in enumerate(zip(row, goal_row)):
        if tile != goal_tile and tile != 0 and tile in goal_row:

            index = goal_row.index(tile)
            # print()
            # print(f"tile={tile}({i})->({index})")
            if i > index:
                # print(f"1- are anything in {row[index:i]} in {goal_row[index + 1:i + 1]}")
                for r in row[index:i]:
                    if r in goal_row[index + 1:i + 1]:
                        # print("CONFLICT!")
                        conflicts += 1
                # if len(set(row[i:index]) & set(goal_row[i + 1:index + 1])) > 0:
                #     conflicts += len(set(row[i:index]) & set(goal_row[i + 1:index + 1]))
                #     print(set(row[i:index]) & set(goal_row[i + 1:index + 1]))
                #     print(f"CONFLICT")
            else:
                # print(f"2- are anything in {row[i + 1:index + 1]} in {goal_row[i:index]}")
                for r in row[i + 1:index + 1]:
                    if r in goal_row[i:index]:
                        # print("CONFLICT!")
                        conflicts += 1
                # if len(set(row[i + 1:index + 1]) & set(goal_row[i:index])) > 0:
                #     conflicts += len(set(row[i + 1:index + 1]) & set(goal_row[i:index]))
                #     print(set(row[i + 1:index + 1]) & set(goal_row[i:index]))
                #     print(f"CONFLICT")

    return conflicts * 2


def linear_heuristic(state, goal_state, number_of_tiles, size):
    distance = manhattan_heuristic(state, goal_state, number_of_tiles, size)
    # print(f"conflicts={distance}")

    for i in range(size):
        # columns
        distance += count_conflicts(state[i::size], goal_state[i::size])
        # rows
        distance += count_conflicts(state[i * size:(i + 1) * size], goal_state[i * size:(i + 1) * size])

    # print(f"conflicts={distance}")
    # exit()
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
    # f = g + manhattan_heuristic(state, goal_state, number_of_tiles, size)
    f = g + linear_heuristic(state, goal_state, number_of_tiles, size)

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

    # print(linear_heuristic(initial_state, goal_state, number_of_tiles, size))
    # exit()

    y = initial_state.index(0)
    # threshold = manhattan_heuristic(initial_state, goal_state, number_of_tiles, size)
    threshold = linear_heuristic(initial_state, goal_state, number_of_tiles, size)
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
