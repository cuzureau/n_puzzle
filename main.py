import sys
from solvability import puzzle_is_solvable
from solver import solve
from heuristics import heuristics
from parser import parser


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


def board_is_valid(board, size):
	if len(board) == size >= 3:
		for row in board:
			if len(row) != size:
				return False
	else:
		return False


def error(name):
	if name == 'open':
		print(f"Error:\n\tfile '{sys.argv[1]}' cannot be open")
	elif name == 'invalid':
		print(f"Error:\n\tthe board is not valid")
	elif name == 'unsolvable':
		print(f"Error:\n\tthe puzzle is unsolvable")
	exit()


def main():
	initial_state, size, heuristic = parser()

	goal_state = define_goal_state(size)
	if puzzle_is_solvable(initial_state, goal_state, size):
		heuristic = heuristics['conflicts']
		path, node_count = solve(heuristic, initial_state, goal_state, size)
		print(f"complexity in time: {node_count}")
		print(f"complexity in space: {len(path)}")
		print(f"number of moves: {len(path) - 1}")
		print(f"initial state to final state:")
		for p in reversed(path):
			print(f"{p}")
	else:
		error('unsolvable')


if __name__ == '__main__':
	main()
