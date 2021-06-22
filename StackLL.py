class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = Node("top")
        self.size = 0

    def push(self, data):
        newnode = Node(data)
        newnode.next= self.top.next
        self.top.next = newnode
        self.size += 1

    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
            return
        removedelement = self.top.next
        self.top.next = self.top.next.next
        self.size -= 1
        print("Popped"+str(removedelement.data))
        return removedelement.data

    def peek(self):
        if self.isEmpty():
            print("Stack Empty")
        return self.top.next.data

    def isEmpty(self):
        return self.size == 0

    def getsize(self):
        return self.size

    def printStack(self):
        currnode = self.top.next
        printstr = ""
        while currnode:
            printstr += str(currnode.data) + " "
            currnode = currnode.next
        print(printstr)


stack = Stack()
for i in range(10):
    stack.push(i)

stack.printStack()

for j in range(11):
    stack.pop()
stack.printStack()
