class Node:
    def __init__(self, data):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rare = None
        self.size = 0

    def enqueue(self, item):
        new_node = Node(item)
        #if queue is empty, both fornt anf rare point to new_node
        if self.isEmpty():
            self.front = self.rare = new_node
        else:
            self.rare.next = new_node
        
        self.size += 1
        print(f"{item} pushed in queue") 

    def dequeue(self):
        if not self.isEmpty():
            item = self.front.data
            self.front = self.front.next
            print(f"Deleted item is {item}")
            self.size -=1
        return None

    def isEmpty(self):
        return self.front == None
    
    def queueSize(self):
        return self.size
    
    def peek(self):
        return self.front.data
    
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    

    #Top element
    print("Top element", q.peek())
    #Print size
    print("Size", q.queueSize())
    #pop
    q.dequeue()
    print("Size after popping element", q.queueSize())

    #Check Queue is empty or not
    print("Empty queue" if q.isEmpty() else f"Queue is not empty it contains {q.queueSize()} elements")






