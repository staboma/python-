class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

arr = [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]
root = None
for key in arr:
    root = insert(root, key)

print("Inorder traversal of the BST:")
inorder_traversal(root)
