class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
        # Khusus AVL
        self.height = 1




print("===== BINARY TREE =====")

# Membuat Binary Tree manual
root_bt = Node(10)

root_bt.left = Node(5)
root_bt.right = Node(20)

root_bt.left.left = Node(3)
root_bt.left.right = Node(7)

print("Root      :", root_bt.key)
print("Left Child:", root_bt.left.key)
print("Right Child:", root_bt.right.key)


# =========================================
# TRAVERSAL BINARY TREE
# =========================================

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

print("\nTraversal Inorder Binary Tree:")
inorder(root_bt)


# =========================================
# BINARY SEARCH TREE (BST)
# =========================================

