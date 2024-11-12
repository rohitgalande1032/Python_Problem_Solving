class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root, arr):
    if not root:
        return 
    arr.append(root.data)
    preorder(root.left, arr)
    preorder(root.right, arr)

    return arr

def inorder(root, arr):
    if not root:
        return
    
    inorder(root.left, arr)
    arr.append(root.data)
    inorder(root.right, arr)

    return arr

def postorder(root, arr):
    if not root: 
        return
    postorder(root.left, arr)
    postorder(root.right, arr)
    arr.append(root.data)

    return arr

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    arr1 = []
    arr2 = []
    arr3 = []

    print(f"Preorder Traversal : {preorder(root, arr1)}")
    print(f"Inorder Tracersal : {inorder(root, arr2)}")
    print(f"Postorder Traversal : {postorder(root, arr3)}")