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


def insert(root, key):
    if not root:
        root = Node(key)
        return root
    q = [root]
    while len(q):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)
    return root


def deleteLowestRightmost(root, nodetodelete):
    q = []
    q.append(root)
    while (len(q)):
        temp = q.pop(0)
        if temp is nodetodelete:
            temp = None
            return
        if temp.right:
            if temp.right is nodetodelete:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is nodetodelete:
                temp.left = None
                return
            else:
                q.append(temp.left)


def deleteNode(root, key):
    if root is None:
        return None
    if root.left is None and root.right is None:
        if root.key == key:
            return None
        else:
            return root
    nodetodelete = None
    q = [root]
    while len(q):
        temp = q.pop(0)
        if temp.key == key:
            nodetodelete = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    if nodetodelete:
        k = temp.key
        deleteLowestRightmost(root, temp)
        nodetodelete.key = k
    return root

root= Node(1)
root.left= Node(2)
root.left.left= Node(3)
root.left.right= Node(4)
root.right= Node(5)
root.right.left= Node(6)
root.right.right= Node(7)

    #             1
    #     2             5
    # 3       4   6           7
# root.inordertraversal()
root= insert(root, 8)
#                 1
#         2             5
#   3       4   6           7
# 8
# root.inordertraversal()

root= deleteNode(root, 5)
#                 1
#         2             8
#   3       4   6           7
root.inordertraversal()
