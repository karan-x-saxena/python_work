from binaryTree import Tree
from LevelTraversal import Level_order

def all_traversal(root,name):
    stack = [[root,1]]
    pre = []
    post = []
    In = []
    while stack:
        node = stack[-1][0]
        val = stack[-1][1]
        if val == 1:
            pre.append(node.data)
            stack[-1][1] = 2
            if node.left:
                stack.append([node.left,1])
        elif val == 2:
            In.append(node.data)
            stack[-1][1] = 3
            if node.right:
                stack.append([node.right,1])
        else:
            post.append(node.data)
            stack.pop()
    if name == "preorder":
        return pre
    elif name == "postorder":
        return post
    elif name == "inorder":
        return In
    else:
        return "enter name or correct name for order!"

if __name__ == '__main__':
    root = Tree(5)
    arr = [3, 4, 7, 6, 8, 1, 0, 2]
    root.insert_element(arr)
    Level_order(root)
    print(all_traversal(root,"inorder"))