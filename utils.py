def is_even(number):
    return number % 2


def manhattan_distance(a, b, size):
    return abs(b // size - a // size) + abs(b % size - a % size)


def count_distance(number, state1, state2, size):
    position1 = state1.index(number)
    position2 = state2.index(number)

    return manhattan_distance(position1, position2, size)


def define_goal_state(length):
    m = [[0] * length for i in range(length)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(length + length - 2):
        for j in range((length + length - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    n = []
    for i in m:
        for j in i:
            n.append(j)

    return tuple(n)
