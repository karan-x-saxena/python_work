from binaryTree import Tree
from traversal import all_traversal
from LevelTraversal import Level_order

def depth_tree(root):
    if root.left is None and root.right is None:
        return 1
    a = -10000000
    b = -10000000
    if root.left:
        a = 1 + depth_tree(root.left)
    if root.right:
        b = 1+depth_tree(root.right)
    return max(a,b)

root = Tree(1)
arr = [0,5,4,3,6]
root.insert_element(arr)
print(depth_tree(root))