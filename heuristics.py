def uniform_cost(state, goal_state, size):
    return 0


def hamming_heuristic(state, goal_state, size):
    res = 0

    for s, g in zip(state, goal_state):
        if s != 0 and s != g:
            res += 1

    return res


def manhattan_heuristic(state, goal_state, size):
    distance = 0

    for i in range(size * size):
        if state[i] != goal_state[i] and state[i] != 0:
            ci = goal_state.index(state[i])
            y = (i // size) - (ci // size)
            x = (i % size) - (ci % size)
            distance += abs(y) + abs(x)

    return distance


def count_conflicts(row, goal_row, size, ans=0):
    counts = [0 for x in range(size)]
    for i, tile in enumerate(row):
        if tile != 0 and tile in goal_row:
            index = goal_row.index(tile)
            if i > index:
                for r in row[index:i]:
                    if r != 0 and r in goal_row[index + 1:i + 1]:
                        counts[i] += 1
            else:
                for r in row[i + 1:index + 1]:
                    if r != 0 and r in goal_row[i:index]:
                        counts[i] += 1

    if max(counts) == 0:
        return ans * 2
    else:
        i = counts.index(max(counts))
        row = [r for r in row]
        row[i] = -1
        ans += 1
        return count_conflicts(row, goal_row, size, ans)


def linear_heuristic(state, goal_state, size):
    distance = manhattan_heuristic(state, goal_state, size)

    for i in range(size):
        # row
        distance += count_conflicts(state[i::size], goal_state[i::size], size)
        # column
        distance += count_conflicts(state[i * size:(i + 1) * size], goal_state[i * size:(i + 1) * size], size)

    return distance


heuristics = {
    'hamming': hamming_heuristic,
    'manhattan': manhattan_heuristic,
    'linear': linear_heuristic,
    'uniform': uniform_cost,
}
