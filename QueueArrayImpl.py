class Queue:
    def __init__(self, capacity):
        self.front=0
        self.size= 0
        self.rear= capacity -1
        self.Q = [None]* capacity
        self.capacity = capacity

    def enqueue(self, data):
        if self.isFull():
            print("Queue is already full")
            return
        self.rear= (self.rear+1) % self.capacity
        self.Q[self.rear] = data
        self.size = self.size+1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is already empty")
            return
        print(str(self.Q[self.front])+" is dequed")
        self.front = (self.front+1)% self.capacity
        self.size -= 1

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def frontqueue(self):
        if self.isEmpty():
            print("Queue is already empty")
            return
        print("Front item is ", self.Q[self.front])

    def rearqueue(self):
        if self.isEmpty():
            print("Queue is already empty")
            return
        print("Rear item is ", self.Q[self.rear])

queue= Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.dequeue()
queue.frontqueue()
queue.rearqueue()