class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Item {item} pushed in queue")

    def dequeue(self):
        if self.isEmpty():
            return None
        item = self.queue.pop()
        print(f"{item} popped from queue")
        return item
    
    def peek(self):
        return self.queue[-1]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    

if __name__ == "__main__":
    q = Queue()
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)

    print("Size: ", q.size())
    print(f"Popped element is {q.dequeue()}")
    print("Size: ", q.size())
    print("Empty Queue" if q.isEmpty() else f"queue is with size {q.size()}")
    print("Top element", q.peek())


