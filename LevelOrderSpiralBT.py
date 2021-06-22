class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def spiralLevelPrint(root):
    if root is None:
        return
    stack1 = []
    stack2 = []
    stack1.append(root)

    while not len(stack1) == 0 or not len(stack2) == 0:
        while not len(stack1) == 0:
            temp = stack1[-1]
            stack1.pop()
            print(temp.key, end=' ')
            if temp.right:
                stack2.append(temp.right)
            if temp.left:
                stack2.append(temp.left)
        while not len(stack2) == 0:
            temp = stack2[-1]
            stack2.pop()
            print(temp.key, end=' ')

            if temp.left:
                stack1.append(temp.left)
            if temp.right:
                stack1.append(temp.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
spiralLevelPrint(root)
