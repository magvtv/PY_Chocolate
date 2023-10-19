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
    
    #revert the suggested instruction on stack 
    def undo(self):
        if self.undo_stack:
            operation, candy = self.undo_stack.pop()
            if operation == 'push':
                # undo the push instruction by removing the candy
                self.stack.pop()
            elif operation == 'pop':
                # undo the pop instruction by returning the candy
                self.stack.append(candy)
                
    def is_empty(self):
        return len(self.stack) == 0