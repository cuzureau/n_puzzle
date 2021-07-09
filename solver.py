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


def search(heuristic, path, g, threshold, goal_state, size, node_count, algorithm, weight):
    node_count += 1
    state = path[0]
    h = heuristic(state, goal_state, size)
    f = algorithm(g, h, weight)

    if f > threshold:
        return f, node_count
    if state == goal_state:
        return True, node_count

    minimum = float('inf')
    nodes = nextnodes(state, size)

    for node in nodes:
        if node not in path:
            path.appendleft(node)
            tmp, node_count = search(heuristic, path, g + 0, threshold, goal_state, size, node_count, algorithm, weight)
            if tmp is True:
                return True, node_count
            if tmp < minimum:
                minimum = tmp
            path.popleft()

    return minimum, node_count


class Node():
    def __init__(self, state, heuristic, count, parent):
        self.state = state
        self.heuristic = heuristic
        self.count = count
        self.parent = parent
        self.f = heuristic + count

    def __str__(self):
        return f"{self.state}(h={self.heuristic})"

    def __lt__(self, other):
        return self.f < other.f

    # def __gt__(self, other):
    #     if isinstance(other, Number):
    #         return self.value > other.value
    #     else:
    #         raise E.Error(self, '>', other)
    #
    # def __eq__(self, other):
    #     if isinstance(other, Number):
    #         return (self.value == other.value)
    #     else:
    #         raise E.Error(self, '==', other)

    def __repr__(self):
    	return f"{self.state}(h={self.heuristic})"

    # def __eq__(self, other):
    # 	return np.array_equal(self.state, other.state)

    # def __hash__(self):
    # 	return hash(self.state.tobytes())


def a_star_algorithm(initial_state, goal_state, size, heuristic):
    from heapq import heappush, heappop, heapify

    initial_node = Node(initial_state, heuristic(initial_state, goal_state, size), 0, None)
    open_list = [initial_node]
    close_list = {}
    heapify(open_list)

    while open_list:
        current_node = heappop(open_list)

        if current_node.state == goal_state:
            path = [current_node.state]
            parent = current_node.parent
            while parent is not None:
                path.append(parent)
                parent = close_list[parent.state]

            print(len(path))
            for p in path:
                print(p)
            return path
        else:
            close_list[current_node.state] = current_node.parent

        nodes = nextnodes(current_node.state, size)
        for node in nodes:
            h = heuristic(node, goal_state, size)
            g = current_node.count + 1
            if node not in open_list:
                t_node = Node(node, h, g, current_node)
                heappush(open_list, t_node)







def solve(initial_state, goal_state, size, algorithm, heuristic, weight):
    # import sys
    # sys.setrecursionlimit(500000)

    a_star_algorithm(initial_state, goal_state, size, heuristic)

    # threshold = heuristic(initial_state, goal_state, size)
    # path = deque([initial_state])
    # node_count = 0
    #
    # while 1:
    #     tmp, node_count = search(heuristic, path, 0, threshold, goal_state, size, node_count, algorithm, weight)
    #     if tmp is True:
    #         return path, node_count
    #     elif tmp == float('inf'):
    #         return False, node_count
    #     else:
    #         threshold = tmp
