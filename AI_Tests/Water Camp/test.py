from collections import deque

def pour_water(state, jug, capacity):
    return (capacity, state[1]) if jug == 0 else (state[0], capacity)

def water_jug(initial, goal, max_x, max_y):
    visited = set()
    queue = deque([(initial, [])])

    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)

        if goal in state:
            return path

        x, y = state
        actions = [
            ("Fill Jug x", (max_x, y)),
            ("Fill Jug y", (x, max_y)),
            ("Empty Jug x", (0, y)),
            ("Empty Jug y", (x, 0)),
            ("Pour x to y", pour_water(state, 0, max_y)),
            ("Pour y to x", pour_water(state, 1, max_x))
        ]

        for action, next_state in actions:
            if next_state not in visited:
                queue.append((next_state, path + [action]))

    return None

initial_state = (0, 0)
goal_state = 2
max_capacity_x = 13
max_capacity_y = 7

solution = water_jug(initial_state, goal_state, max_capacity_x, max_capacity_y)

if solution:
    for i, step in enumerate(solution):
        print(f"Step {i + 1}: {step}")
else:
    print("No solution found.")
