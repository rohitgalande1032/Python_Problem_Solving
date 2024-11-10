class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

#Inser node at beginning
def insertHead(head, val):
    newNode = Node(val, head)
    return newNode

#Traverse the list
def printList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

#delete last node 
def deleteLastNode(head):
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
    return head

#Find length of LL    
def lengthOfList(head):
    count = 0
    temp = head
    while temp is not None:
        count += 1
        temp = temp.next
    return count
    
#Check element is present or not
def serchElement(head, element):
    while head is not None:
        if head.data  == element:
            return True
        head = head.next
    return False

#Find the middle of linked list
def findMiddle(head):
    length = lengthOfList(head)
    middle = length//2 
    for i in range(middle):
        head = head.next
    return head
        
#Find midlle node of LL using Tortoise and Hare algorithm(optimised solution) 
def midSlowFast(head):
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

#Reverse the linkedlist using stack or recursive method
def reverseList(head):
    temp = head
    stack = []

    while temp:
        stack.append(temp.data)
        temp = temp.next
    
    temp = head
    while temp:
        temp.data = stack.pop()
        temp = temp.next
    return head


# Reverse Linked List using the changing links between nodes
def reverseLst(head):
    temp = head
    prev = None

    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev

#Detect loop in the Linked List using Tortoise and Hare Algo
def detectLoop(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow==fast:
            return True
    return False

#Detect loop using the extra space
def detectLoopWithMap(head):
    temp = head
    node_set = set()

    while temp:
        if temp in node_set:
            return True
        else:
            node_set.add(temp)
            temp=temp.next
    return False

# Find the firstNode where cycle begins
def firstNode(head):
    temp = head
    node_map = {}

    while temp:
        if temp in node_map:
            return temp
        node_map[temp] = True
        temp = temp.next
    return None

# Find the firstNode where cycle begin using Tortoise ad Hare method
def firstNodeInCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head

            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None

# Find the length of loop in Linked List
def lengthOfLoop(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            count = 1

            while fast.next != slow:
                fast = fast.next
                count += 1
            return count
    return 0

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    val = 5
    
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])


    #To check the loop is present or not

    # head = Node(arr[0])
    # second = Node(arr[1])
    # third = Node(arr[2])
    # fourth = Node(arr[3])
    # fifth = Node(arr[4])

    # head.next = second
    # second.next = third
    # third.next = fourth
    # fourth.next = fifth
    # fifth.next = second
    
    
    print("Original List")
    printList(head)
    
    
    # head = insertHead(head, val)
    # print("\nList after inserting element at start")
    # printList(head)
    
    # deleteLastNode(head)
    # print("\nAfter deleting last node")
    # printList(head) 
    
    print("\nLength of List is", lengthOfList(head))
    
    seerchEle = "Element Found" if serchElement(head, 3) else "Element not Found"
    print(seerchEle)

    #this is brute force approach
    middle = findMiddle(head)
    print("middle is: ", middle.data) 

    #optimized approach to find middle of linkedlist using slow and fast pointer
    mid = midSlowFast(head)
    print("Middle element using Tortoise and Hare Algo ", mid.data)

    print("\nLength of List is", lengthOfList(head))

    reverseLst = reverseList(head)
    #print(reverseNodeChange)
    print("reverse Linked List")
    printList(head)

    detectLoopinLL = detectLoopWithMap(head)
    print("\n")
    print("Loop is present" if detectLoopinLL else "No loop in LinkedList")