class Node:
    def __init__(self, data):
        self.data= data
        self.next= None
        self.prev= None

class DoublyLinkedList:
    def __init__(self):
        self.head= None

    def insert_at_end(self, data):
        newnode= Node(data)
        if self.head is None:
            self.head= newnode
            return
        currnode= self.head
        while currnode.next is not None:
            currnode= currnode.next
        currnode.next= newnode
        newnode.prev = currnode
        return

    def insert_at_beg(self, data):
        newnode= Node(data)
        if self.head is None:
            self.head = newnode
            return
        newnode.next= self.head
        self.head.prev= newnode
        self.head= newnode

    def printLLforward(self):
        if self.head is None:
            print("Linked List is empty")
            return
        currnode= self.head
        while currnode is not None:
            print(currnode.data, " ")
            currnode= currnode.next
        return

    def printLLbackward(self):
        if self.head is None:
            print("Linked List is empty")
            return
        currnode= self.head
        while currnode.next is not None:
            currnode = currnode.next
        while currnode is not None:
            print(currnode.data, " ")
            currnode = currnode.prev
        return

    def insert_after(self, place, data):
        currnode= self.head
        while currnode is not None:
            if currnode.data == place:
                break
            currnode= currnode.next
        if currnode is None:
            print("place is not present in the Linked List")
        else:
            newnode= Node(data)
            newnode.prev = currnode
            newnode.next= currnode.next
            if currnode.next is not None:
                currnode.next.prev= newnode
            currnode.next= newnode
        return

    def delete_element(self, data):
        if self.head is None:
            print("LinkedList is empty")
            return
        if self.head.data == data:
            self.head.next.prev= None
            self.head = self.head.next
            return
        currnode= self.head
        while currnode.next is not None:
            if currnode.next.data==data:
                break
            currnode= currnode.next
        if currnode is None:
            print("Element to be deleted was not found")
        else:
            currnode.next = currnode.next.next
            currnode.next.prev = currnode

    def reverse_ll(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        prev = self.head
        currnode = prev.next
        prev.next = None
        prev.prev = currnode

        while currnode is not None:
            currnode.prev= currnode.next
            currnode.next = prev
            prev = currnode
            currnode = currnode.prev
        self.head = prev
        return

newdoublyll= DoublyLinkedList()
newdoublyll.insert_at_end(1)
newdoublyll.insert_at_end(2)
newdoublyll.insert_after(1, 1.5)
newdoublyll.delete_element(1.5)
newdoublyll.insert_at_end(3)
newdoublyll.insert_at_end(4)
newdoublyll.insert_at_end(5)
newdoublyll.reverse_ll()
newdoublyll.printLLforward()
