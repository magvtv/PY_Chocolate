from main import transition_model, actions

def format_step(action, remaining):
    if action.startwith("Fill"):
        return f"Fill the {action.split()[1]} jar"
    elif action.startswith("Pour"):
        return f"Pour {action.split()[-1]} gallons into the {'x' if 'X' in action else 'y'} jar, {remaining} gallons left in the {'y' if 'Y' in action else 'x'} jar"
    elif action.startswith("Empty"):
        return f"Empty the {'x' if 'X' in action else 'y'} jar"
    else:
        return "Unknown action"