# Experiment No. 2
# BFS for Water Jug Problem

from collections import deque


def water_jug_bfs(capacity_a, capacity_b, target):
    start = (0, 0)

    queue = deque()
    queue.append((start, [start]))

    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        if a == target or b == target:
            return path

        next_states = []

        # Fill Jug A
        next_states.append((capacity_a, b))

        # Fill Jug B
        next_states.append((a, capacity_b))

        # Empty Jug A
        next_states.append((0, b))

        # Empty Jug B
        next_states.append((a, 0))

        # Pour A into B
        transfer = min(a, capacity_b - b)
        next_states.append((a - transfer, b + transfer))

        # Pour B into A
        transfer = min(b, capacity_a - a)
        next_states.append((a + transfer, b - transfer))

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    return None


capacity_a = 4
capacity_b = 3
target = 2

solution = water_jug_bfs(capacity_a, capacity_b, target)

if solution:
    print("Solution found using BFS:")
    for i, state in enumerate(solution):
        print(f"Step {i}: Jug A = {state[0]}L, Jug B = {state[1]}L")
else:
    print("No solution exists.")