from collections import deque


def clone_and_swap(data, y0, y1):
    clone = list(data)
    tmp = clone[y0]
    clone[y0] = clone[y1]
    clone[y1] = tmp

    return tuple(clone)


def nextnodes(state, size):
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
    if y + size < size * size:
        down = clone_and_swap(state, y, y + size)
        res.append(down)

    return res

WEIGHT = 9


def search(heuristic, path, g, threshold, goal_state, size, node_count):
    state = path[0]
    f = g + heuristic(state, goal_state, size) * WEIGHT

    # h = heuristic(state, goal_state, size)
    # if g < h:
    #     f = g + h
    # else:
    #     f = (g + (2 * WEIGHT - 1) * h) / WEIGHT

    node_count += 1

    if f > threshold:
        return f, node_count
    if state == goal_state:
        return True, node_count

    minimum = float('inf')
    nodes = nextnodes(state, size)

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
    import sys
    sys.setrecursionlimit(500000000)

    threshold = heuristic(initial_state, goal_state, size)
    path = deque([initial_state])
    node_count = 0

    while 1:
        tmp, node_count = search(heuristic, path, 1, threshold, goal_state, size, node_count)
        if tmp is True:
            return path, node_count
        elif tmp == float('inf'):
            return False, node_count
        threshold = tmp
