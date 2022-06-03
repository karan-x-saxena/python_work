from binaryTree import Tree

def Level_order(root):
    if root is None:
        return "tree is empty!"
    else:
        que = []
        ans = []
        que.append(root)
        while que:
            level = []
            size = len(que)
            for i in range(size):
                temp = que[0]
                que.remove(que[0])
                if temp.left: que.append(temp.left)
                if temp.right: que.append(temp.right)
                level.append(temp.data)
            ans.append(level)
        return ans
if __name__ == '__main__':
    root = Tree(5)
    arr = [3,4,7,6,8,1,0,2]
    root.insert_element(arr)
    print(Level_order(root))