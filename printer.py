def display(path, node_count):
    print(f"number of moves: {len(path) - 1}")
    print(f"initial state to final state:")
    for p in reversed(path):
        print(f"{p}")
    print(f"complexity in space: {len(path)}")
    print(f"complexity in time: {node_count}")
