class Stack:
    def __init__(self):
        self.stack = list()
        self.maxsize = 5
        self.top = 0

    def push(self, data):
        if self.top >= self.maxsize:
            print("Stack overflow")
        self.stack.append(data)
        self.top += 1
        return

    def pop(self):
        if self.top <= 0:
            print("Stack underflow")
            return
        stacktop = self.stack.pop()
        self.top -= 1
        return stacktop

    def size(self):
        print(str(self.top))
        return self.top

    def peek(self):
        if self.top <= 0:
            print("Stack is empty")
            return
        stacktop = self.stack[self.top-1]
        print(stacktop)

stack= Stack()
stack.push(1)
stack.push(2)
stack.pop()
stack.peek()
stack.size()