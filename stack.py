import numpy as np


m = [[0] * 4 for i in range(4)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y, c = 0, -1, 1
for i in range(4 + 4 - 2):
	for j in range((4 + 4 - i) // 2):
		x += dx[i % 4]
		y += dy[i % 4]
		m[x][y] = c
		c += 1


BOARD_LENGTH = 4
GOAL_STATE = np.array(m)


def goal_on_row(num, i):
	for j in range(BOARD_LENGTH):
		if num == GOAL_STATE[i][j]:
			return j


def goal_on_column(num, j):
	for i in range(BOARD_LENGTH):
		if num == GOAL_STATE[i][j]:
			return i

def linear_conflict_heuristic(state):
	result = 0
	for i in range(BOARD_LENGTH):
		for j in range(BOARD_LENGTH):
			num = state[i][j]
			if num != 0:
				position = goal_on_row(num, i)
				if position is not None:
					if position <= j:
						for k in reversed(range(j)):
							num2 = state[i][k]
							if num2 != 0:
								position2 = goal_on_row(num2, i)
								if position2 is not None:
									if position < position2:
										result += 1
					else:
						for k in range(j + 1, BOARD_LENGTH):
							num2 = state[i][k]
							if num2 != 0:
								position2 = goal_on_row(num2, i)
								if position2 is not None:
									if position > position2:
										result += 1

				position = goal_on_column(num, j)
				if position is not None:
					if position <= i:
						for k in reversed(range(i)):
							num2 = state[k][j]
							if num2 != 0:
								position2 = goal_on_column(num2, j)
								if position2 is not None:
									if position < position2:
										result += 1
					else:
						for k in range(i + 1, BOARD_LENGTH):
							num2 = state[k][j]
							if num2 != 0:
								position2 = goal_on_column(num2, j)
								if position2 is not None:
									if position > position2:
										result += 1
	
	return result


def main():
	state = np.array([[11, 3, 4, 2], [14, 8, 12, 9], [5, 0, 13, 6], [7, 15, 1, 10]])
	result = linear_conflict_heuristic(state)
	print(f"RESULT = {result}")


if __name__ == '__main__':
	main()