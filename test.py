from time import perf_counter as pc

import numpy as np

GOAL_STATE = [[]]
GLOBAL_STATE_DICT = {}
N = 0


class Node:
    def __init__(self, state, manhattan, zero_pos):
        self.state = state
        self.heuristic = manhattan
        self.zero_pos = zero_pos

    def __str__(self):
        return f"state=\n{self.state}\nheuristic={int(self.heuristic)}"

    def __eq__(self, other):
        return np.array_equal(self.state, other.state)

    def __repr__(self):
        return f"state=\n{self.state}\nheuristic={int(self.heuristic)}"

    def __hash__(self):
        return hash(self.state.tobytes())


def customSort(node):
    return node.heuristic


def nextnodes(node):
    zero = node.zero_pos

    r, c = map(int, zero)
    directions = ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
    nodes = []
    for direction in directions:
        if 0 <= direction[0] < N and 0 <= direction[1] < N:
            tmp = np.copy(node.state)
            goal = GLOBAL_STATE_DICT[tmp[direction]]

            tmp[direction], tmp[zero] = tmp[zero], tmp[direction]

            dir_goal_distance = manhattan_distance(direction, goal)
            goal_zero_distance = manhattan_distance(goal, (r, c))

            nodes.append(Node(tmp, node.heuristic - dir_goal_distance + goal_zero_distance, direction))
    return sorted(nodes, key=customSort)


def manhattan_distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def manhattan_heuristic(state):
    distance = 0
    for i in range(N):
        for j in range(N):
            num = state[i][j]
            if num != GOAL_STATE[i][j] and num != 0:
                goal = GLOBAL_STATE_DICT[num]
                distance += manhattan_distance((i, j), goal)
    return distance


def search(path, g, threshold):
    node = list(path.keys())[-1]

    f = g + node.heuristic

    if f > threshold:
        return f
    if np.array_equal(node.state, GOAL_STATE):
        return True

    minimum = float('inf')
    for n in nextnodes(node):
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
    zero = np.where(initial_state == 0)
    initial_node = Node(initial_state, manhattan_heuristic(initial_state), zero)
    threshold = initial_node.heuristic
    # The dictionary keeps insertion order since Python 3.7 so it can be used as a queue
    path = {initial_node: None}
    while 1:
        tmp = search(path, 0, threshold)
        if tmp == True:
            print("GOOD!")
            return path.keys()
        elif tmp == float('inf'):
            print("WRONG!")
            return False
        threshold = tmp



def define_goal_state(n):
    global GOAL_STATE
    global N
    global GLOBAL_STATE_DICT

    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 2):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1

    GOAL_STATE = np.array(m)
    N = len(GOAL_STATE)
    GLOBAL_STATE_DICT = {m[r][c]: (r, c) for r in range(N) for c in range(N)}


tests = {'3x3': np.array([[4, 2, 5], [1, 0, 6], [3, 8, 7]]),
         '4x4': np.array([[15, 7, 9, 3], 
                            [14, 11,  2, 13], 
                            [ 1,  0,  4,  6], 
                            [12,  8,  5, 10]])}

for name, puzzle in tests.items():
    define_goal_state(len(puzzle))
    print('Puzzle:\n', puzzle)
    t0 = pc()
    path = solve(puzzle)
    t1 = pc()
    print(f'{name} depth:{len(path)} runtime:{round(t1 - t0, 3)} s')
    # print(path)