import tkinter as tk

def push_candy():
    global current_candy_index
    candy = candy_entry.get()
    candy_stack.append(candy)
    action_stack.append(('push', candy))
    current_candy_index = len(candy_stack)
    update_display()

def pop_candy():
    global current_candy_index
    if current_candy_index > 0:
        popped_candy = candy_stack.pop()
        action_stack.append(('pop', popped_candy))
        candy_stack.pop()
        current_candy_index = len(candy_stack)
        update_display()

def undo_action():
    global current_candy_index
    if action_stack:
        action, item = action_stack.pop()
        if action == 'push':
            candy_stack.pop()
            current_candy_index = len(candy_stack)
        elif action == 'pop':
            candy_stack.append(item)
            current_candy_index = len(candy_stack)
    update_display()

def update_display():
    candy_display.config(text='\n'.join(f'{x + 1}.{candy}' for x, candy in enumerate(candy_stack) ))

root = tk.Tk()
root.title("Candy Dispenser")

# List of candy items
candy_stack = [
    "Snickers", 
    "Baby Ruth", 
    "Kitkat", 
    "M&Ms", 
    "Hershey",
    "Twix"
]

current_candy_index = len(candy_stack)
# current_candy_index = 0
action_stack = []

# Create entry field for candy input, buttons and placing their widgets
candy_entry = tk.Entry(root)
candy_entry.pack()
push_button = tk.Button(root, text='PUSH', command=push_candy)
push_button.pack()
pop_button = tk.Button(root, text='POP', command=pop_candy)
pop_button.pack()
undo_button = tk.Button(root, text='UNDO', command=undo_action)
undo_button.pack()

# Create a label to display the candy
candy_display = tk.Label(root, text='\n'.join(f'{x + 1}.{candy}' for x, candy in enumerate(candy_stack)), font=("Handlee", 14))
candy_display.pack()
# Place widgets in the GUI

root.mainloop()
