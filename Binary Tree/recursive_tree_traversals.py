# Preorder Traversal: Root → Left → Right
# Inorder Traversal: Left → Root → Right
# Postorder Traversal: Left → Right → Root

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if not root:
        return
    
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def postorder(root):
    if not root: 
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")
    

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)


    print("Preorder Traversal")
    preorder(root)
    print("\nInorder Tracersal")
    inorder(root)
    print("\nPostorder Traversal")
    postorder(root)