from collections import deque
from template import format_output

# defining initial state, goal state - need to add goal state = (0,2)
initial_state = (0,0)
goal_state = (2,0)


# define the capacity of the non-graduated jars
max_capacity_x = 13
max_capacity_y = 7

actions = [
    (f"Fill X", lambda state: (max_capacity_x, state[1])),
    (f"Fill Y", lambda state: (state[0], max_capacity_y)),
    (f"Pour X to Y", lambda state: (max(0, state[0] - (max_capacity_y - state[1])), min(state[0] + state[1], max_capacity_y))),
    (f"Pour Y to X", lambda state: (min(0, state[0] + state[1], max_capacity_x), max(0, state[1] - (max_capacity_y - state[0])))),
    (f"Empty X", lambda state: (0, state[1])),
    (f"Empty Y", lambda state: (state[0], 0))
]


def transition_model(state, action):
    return action(state)

def breadth_first_search(initial_state, goal_state, actions, transition_model):
    queue = deque([(initial_state, [])])
    explored = set()
    
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path
        
        for action_name, action_function in actions:
            next_state = transition_model(state, action_function)
            if next_state not in explored:
                queue.append((next_state, path + [action_name]))
                explored.add(next_state)
                
    return None


solution = breadth_first_search(initial_state, goal_state, actions, transition_model)

if solution:
    print("Solution Found!")
    print("Steps to take\n")
    for i, step in enumerate(format_output(solution)):
        print(f"{i + 1}. {step}")
else:
    print("No solution found for this one!")