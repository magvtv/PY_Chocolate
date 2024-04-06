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
        
        
        if state[0] == goal or state[1] == goal:
            return path
        
        x, y = state
        actions = [
            ("Fill Jug X", (max_x, y)),
            ("Fill Jug Y", (x, max_y)),
            ("Empty Jug X", (0, y)),
            ("Empty Jug Y", (x, 0)),
            ("Pour X into Y", pour_water(state, 1, min(y + x, max_y))),
            ("Pour Y into X", pour_water(state, 0, min(x + y, max_x)))
        ]
        
        for action, next_state in actions:
            if next_state not in visited:
                queue.append((next_state, path + [action]))
                
    return None
        
# defining initial state, goal state - need to add goal state = (0,2)
initial_state = (0,0)
goal_state = 2

# define the capacity of the non-graduated jars
max_capacity_x = 13
max_capacity_y = 6

solution = water_jug(initial_state, goal_state, max_capacity_x, max_capacity_y)

if solution:
    print("Steps to take\n")
    for i, step in enumerate(solution):
        print(f"{i + 1}. {step}")
else:
    print("No solution found!")