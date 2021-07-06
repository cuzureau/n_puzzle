from collections import deque
from heuristics import heuristics


class Node:
    def __init__(self, state, heuristic):
        self.state = state
        self.heuristic = heuristic

    def __str__(self):
        return f"state=\n{self.state}\nheuristic={int(self.heuristic)}"

    def __eq__(self, other):
        return self.state == other
    #
    # def __repr__(self):
    #     return f"state=\n{self.state}\nheuristic={int(self.heuristic)}"

    def __hash__(self):
        return hash(self.state.tobytes())


def customSort(node):
    return node.heuristic


def clone_and_swap(data, y0, y1):
    clone = list(data)
    tmp = clone[y0]
    clone[y0] = clone[y1]
    clone[y1] = tmp

    return tuple(clone)


def nextnodes(state, goal_state, size, heuristic):
    res = []
    y = state.index(0)

    if y % size > 0:
        left = clone_and_swap(state, y, y - 1)
        res.append(Node(left, heuristic(left, goal_state, size)))
    if y % size + 1 < size:
        right = clone_and_swap(state, y, y + 1)
        res.append(Node(right, heuristic(right, goal_state, size)))
    if y - size >= 0:
        up = clone_and_swap(state, y, y - size)
        res.append(Node(up, heuristic(up, goal_state, size)))
    if y + size < size * size:
        down = clone_and_swap(state, y, y + size)
        res.append(Node(down, heuristic(down, goal_state, size)))

    res.sort(key=customSort)
    return res


def search(heuristic, path, g, threshold, goal_state, size, node_count):
    state = path[0]
    f = g + heuristic(state, goal_state, size)
    node_count += 1

    if f > threshold:
        return f, node_count
    if state == goal_state:
        return True, node_count

    minimum = float('inf')
    nodes = nextnodes(state, goal_state, size, heuristic)
    for node in nodes:
        if node not in path:
            path.appendleft(node)
            tmp, node_count = search(heuristic, path, g + 1, threshold, goal_state, size, node_count)
            if tmp is True:
                return True, node_count
            if tmp < minimum:
                minimum = tmp
            path.popleft()

    return minimum, node_count


def solve(heuristic, initial_state, goal_state, size):
    threshold = heuristic(initial_state, goal_state, size)
    path = deque([initial_state])
    node_count = 0

    while 1:
        tmp, node_count = search(heuristic, path, 0, threshold, goal_state, size, node_count)
        if tmp is True:
            return path, node_count
        elif tmp == float('inf'):
            return False, node_count
        threshold = tmp
