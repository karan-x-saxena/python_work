class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def push_element(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.push_element(data)
            else:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.push_element(data)
        else:
            self.data = data

    def insert_element(self,arr):
        for i in arr:
            self.push_element(i)

