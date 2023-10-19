import tkinter as tk

class PezDispenser:
    def __init__(self):
        self.stack = []
        self.undo_stack = []

    # add or push candy to stack
    def push(self, candy):
        self.stack.append(candy)
        self.undo_candy.append(('push', candy))
        
    # pop candy from stack
    def pop(self):
        if not self.is_empty():
            candy = self.stack.pop()
            self.undo_stack.append(('pop', candy))
            return candy
        else:
            return None
    
    #revert the suggested action on stack 
    def undo(self):
        if self.undo_stack:
            operation, candy = self.undo_stack.pop()
            if operation == 'push':
                # undo the push action by removing the candy
                self.stack.pop()
            elif operation == 'pop':
                # undo the pop action by returning the candy
                self.stack.append(candy)
                
    def is_empty(self):
        return len(self.stack) == 0
    
class CandyDispenserApp:
    def __init__(self, root):
        self.root = root
        self.root.title = ('PEZ Candy Dispenser')
        self.pez_dispenser = PezDispenser()
        self.label = tk.Label(root, text='PEZ Candy Dispenser')
        self.label.pack
        
        self.candy_entry = tk.Entry(root)
        self.candy_entry.pack()
        
        self.push.button = tk.Button(root, text='PUSH', command=self.push_candy)
        self.push_button.pack()
        
        self.pop.button = tk.Button(root, text='POP', command=self.pop_candy)
        self.pop_button.pack()
        
        self.undo.button = tk.Button(root, text='UNDO', command=self.undo_action)
        self.undo_button.pack()
    
    def push_candy(self):
        candy = self.candy_entry.get()
        if candy:
            self.pez_dispenser.push(candy)
            self.candy_entry.delete(0, tk.END)

    def pop_candy(self):
        candy = self.pez_dispenser.pop()
        if candy:
            message = f'Popped: {candy}'
        else:
            message = f'Dispenser is empty'

    def undo_action(self):
        self.pez_dispenser.undo()
        self.show_message("Undo")
        
    def show_message(self, message):
        message_label = tk.Label(self.root, text=message)
        message_label.pack()
        
if __name__ == '__main__':
    root = tk.Tk()
    app = CandyDispenserApp(root)
    root.mainloop()
    
    