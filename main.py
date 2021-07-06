from solvability import puzzle_is_solvable
from solver import solve
from heuristics import heuristics
from parser import parser
from utils import define_goal_state


def main():
    try:
        initial_state, size, heuristic = parser()
    except TypeError:
        exit()

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
        print('Sadly... puzzle initial state is unsolvable.')


if __name__ == '__main__':
    main()
