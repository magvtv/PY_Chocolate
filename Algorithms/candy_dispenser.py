import tkinter as tk
    
class CandyDispenserApp:
    def __init__(self, root):
        self.root = root
        self.root.title = ('Candy Dispenser')
        
        self.candy_stack = ['Amanda','Bulgaria','Chelsea','Daisy','Elodie','Florence','Georgia','Hazel','Jasmine']
        
        self.current_candy_index = 0
        
        self.candy_entry = tk.Entry(root)
        self.candy_entry.pack()
        self.push_button = tk.Button(root, text='PUSH', command=self.push_candy)
        self.push_button.pack()
        self.pop_button = tk.Button(root, text='POP', command=self.pop_candy)
        self.pop_button.pack()
        self.undo_button = tk.Button(root, text='UNDO', command=self.undo_action)
        self.undo_button.pack()
        
        
        
    def candy_display(self):
        self.candy_entry.delete(0, 'end')
        self.candy_entry.insert(0, ' '.join(self.candy_stack))
    def push_candy(self):
        candy = self.candy_entry.get()
        self.candy_stack.insert(self.current_candy_index, candy)
        self.current_candy_index += 1
        self.candy_display()
        
    def pop_candy(self):
        if (self.current_candy_index > 0):
            self.candy_stack.pop(self.current_candy_index - 1)
            self.current_candy_index -= 1
            self.candy_display()
            
    def undo_action(self):
        if (self.current_candy_index > 0):
            self.current_candy_index -= 1
            self.candy_display()
    
        
if __name__ == '__main__':
    root = tk.Tk()
    app = CandyDispenserApp(root)
    root.mainloop()
    
    