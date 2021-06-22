class Node:
    def __init__(self, data):
        self.data= data
        self.next = None

class Queue:
    def __init__(self):
        self.front= self.rear= None

    def enqueue(self, data):
        newnode= Node(data)
        if self.rear is None:
            self.front= self.rear= newnode
            return
        self.rear.next = newnode
        self.rear = newnode

    def dequeue(self):
        if self.isEmpty():
            print("Queue is already empty")
            return
        temp= self.front
        self.front= temp.next
        if self.front is None:
            self.rear = None

    def isEmpty(self):
        return self.front == None

queue= Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.front.data)
print(queue.rear.data)
queue.dequeue()
queue.dequeue()
queue.dequeue()

