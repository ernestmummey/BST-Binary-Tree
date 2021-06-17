class BST:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
###################################################################
# Recursive
###################################################################
    def insert(self, value):
        if value < self.value:
            if value.left is None:
                value.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if value.right is None:
                value.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value):
        pass

    def remove(self, value):
        pass


