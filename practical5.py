# Experiment No. 5
# 8-Puzzle using A* Algorithm

import heapq


goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def manhattan_distance(state):
    distance = 0

    for i, value in enumerate(state):
        if value == 0:
            continue

        goal_index = goal.index(value)

        r1, c1 = divmod(i, 3)
        r2, c2 = divmod(goal_index, 3)

        distance += abs(r1 - r2) + abs(c1 - c2)

    return distance


def neighbors(state):
    result = []

    zero = state.index(0)
    row, col = divmod(zero, 3)

    for dr, dc in [(-1, 0), (1, 0),
                   (0, -1), (0, 1)]:

        nr = row + dr
        nc = col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_zero = nr * 3 + nc

            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            result.append(tuple(new_state))

    return result


def a_star(start):
    open_list = []

    g = 0
    h = manhattan_distance(start)

    heapq.heappush(
        open_list,
        (g + h, g, start, [start])
    )

    visited = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path

        for next_state in neighbors(state):

            if next_state not in visited:
                new_g = g + 1
                new_h = manhattan_distance(next_state)

                heapq.heappush(
                    open_list,
                    (new_g + new_h,
                     new_g,
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

solution = a_star(start)

print("A* Solution:")

for step, state in enumerate(solution):
    print("Step", step)
    display(state)