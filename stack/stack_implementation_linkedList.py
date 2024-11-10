class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print(f"item pushed in stack is {item}")

    def pop(self):
        if self.is_empty():
            print("Empty stack")
            return None
        popped_item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_item
    
    def is_empty(self):
        return self.top == None
    
    def stackSize(self):
        return self.size
    
    def Top(self):
        return self.top.data
    

if __name__ ==  "__main__":
    s = Stack()
    s.push(3)
    s.push(4)
    s.push(5)

    print("Size : ", s.stackSize())
    print("Top", s.Top())
    print("Empty" if s.is_empty() else f"Not empty, size is {s.stackSize()}")
    print(f"Popped Element is {s.pop()}")
    print("Top after deletion", s.Top())
    print("Size after deletion: ", s.stackSize())

        
