class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    

if __name__ == "__main__":
    s = Stack()
    s.push(6)
    s.push(3)
    s.push(7)
    print("Top of stack is before deleting any element", s.top())
    print("Size", s.size())
    print("Empty stack" if s.is_empty() else f"size of stack is {s.size()}")
    s.pop()
    print("Top of stack is after deleting any element", s.top())
    print("Size", s.size())