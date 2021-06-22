class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def preordertraversal(self):
        print(self.key, end=' ')
        if self.left:
            self.left.preordertraversal()
        if self.right:
            self.right.preordertraversal()

    def inordertraversal(self):
        if self.left:
            self.left.inordertraversal()
        print(self.key, end=' ')
        if self.right:
            self.right.inordertraversal()

    def postordertraversal(self):
        if self.left:
            self.left.postordertraversal()
        if self.right:
            self.right.postordertraversal()
        print(self.key, end=' ')

    def insert(self, key):
        if not self.key:
            self.key = key
            return
        if self.key == key:
            return
        if key < self.key:
            if self.left:
                self.left.insert(key)
                return
            self.left = Node(key)
            return
        if key > self.key:
            if self.right:
                self.right.insert(key)
                return
            self.right = Node(key)

    def getmin(self):
        currnode = self
        while currnode.left is not None:
            currnode = currnode.left
        return currnode.key

    def getmax(self):
        currnode = self
        while currnode.right is not None:
            currnode = currnode.right
        return currnode.key

    def delete(self, key):
        if self is None:
            return None
        if key < self.key:
            self.left = self.left.delete(key)
            return self
        if key > self.key:
            self.right = self.right.delete(key)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        minrightsubtree = self.right
        while minrightsubtree.left:
            minrightsubtree = minrightsubtree.left
        self.key = minrightsubtree.key
        self.right = self.right.delete(minrightsubtree.key)
        return self

    def search(self, key):
        if key == self.key:
            return True
        if key < self.key:
            if self.left is None:
                return False
            return self.left.search(key)
        if key> self.key:
            if self.right is None:
                return False
            return self.right.search(key)