import sys


class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.front = 1

    def buildheap(self):
        n = self.size
        for posn in range(n // 2, 0, -1):
            self.heapify(posn)

    def heapify(self, posn):
        if not self.isLeaf(posn):
            if self.Heap[posn] > self.Heap[self.leftChild(posn)] or self.Heap[posn] > self.Heap[self.rightChild(posn)]:
                if self.Heap[self.leftChild(posn)] < self.Heap[self.rightChild(posn)]:
                    self.swap(posn, self.leftChild(posn))
                    self.heapify(self.leftChild(posn))
                else:
                    self.swap(posn, self.rightChild(posn))
                    self.heapify(self.rightChild(posn))

    def leftChild(self, posn):
        return 2 * posn

    def rightChild(self, posn):
        return (2 * posn) + 1

    def isLeaf(self, posn):
        if self.size // 2 <= posn <= self.size:
            return True
        return False

    def swap(self, posn1, posn2):
        self.Heap[posn1], self.Heap[posn2] = self.Heap[posn2], self.Heap[posn1]

    def insert(self, key):
        if self.size >= self.maxsize:
            print("Heap is already full")
            return
        self.size += 1
        self.Heap[self.size] = key

        curr = self.size
        while self.Heap[curr] < self.Heap[self.parent(curr)]:
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)

    def parent(self, posn):
        return posn // 2

    def popmin(self):
        popped = self.Heap[self.front]
        self.Heap[self.front] = self.Heap[self.size]
        self.size -= 1
        self.heapify(self.front)
        return popped

    def printheap(self):
        for i in range(1, (self.size // 2) + 1):
            print(" parent: " + str(self.Heap[i]), end=' ')
            if self.size > 2 * i:
                print(" left child: " + str(self.Heap[2 * i]), end=' ')
            if self.size > 2 * i + 1:
                print(" right child " + str(self.Heap[(2 * i) + 1]))


minHeap = MinHeap(10)
minHeap.insert(3)
minHeap.insert(6)
minHeap.insert(4)
minHeap.insert(8)
minHeap.insert(1)
minHeap.insert(2)
minHeap.insert(5)
minHeap.insert(7)
minHeap.insert(9)
minHeap.insert(10)
minHeap.insert(11)
minHeap.buildheap()

minHeap.printheap()
print(str(minHeap.popmin()))
