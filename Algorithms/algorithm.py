# wanna learn on algorithms with python. just one would do.
"""
    states in the usa: Washington, Illnois, Mississippi, Texas, Nebraska, Arizona, Wyoming
    South Dakota, North Carolina, Utah, Iowa, Alburquque
"""
    
class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next
def __init__(self):
    self.head = None
    self.size = 0
def __len__(self):
    return self.size
def is_empty(self):
    return self.size == 0

def push(self, x):
    self.head = self.Node(x, self.head)
    self.size += 1
    
def top(self):
    if self.is_empty():
        raise "Linked list is empty"
    return self.head.element
    
    
node1 = Node("LAX", "MSP")
node2 = Node("MSP", "SDT")
node3 = Node("SDT", "TXS")

