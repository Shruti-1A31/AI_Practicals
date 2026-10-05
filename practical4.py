# Experiment No. 4
# 8-Puzzle using Heuristic Function
# Heuristic: Manhattan Distance

import heapq


goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def manhattan_distance(state):
    distance = 0

    for i, value in enumerate(state):
        if value != 0:
            goal_index = goal.index(value)

            current_row = i // 3
            current_col = i % 3

            goal_row = goal_index // 3
            goal_col = goal_index % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def heuristic_search(start):
    priority_queue = []
    heapq.heappush(priority_queue,
                   (manhattan_distance(start), start, [start]))

    visited = set()

    while priority_queue:
        h, state, path = heapq.heappop(priority_queue)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path

        for next_state in get_neighbors(state):
            if next_state not in visited:
                heapq.heappush(
                    priority_queue,
                    (manhattan_distance(next_state),
                     next_state,
                     path + [next_state])
                )

    return None


def display(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()


start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

solution = heuristic_search(start)

print("Initial State:")
display(start)

print("Solution Path:")

for step, state in enumerate(solution):
    print("Step", step)
    display(state)