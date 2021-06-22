class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

class SinglyLinkedList:
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
        return

    def insert_at_beg(self, data):
        newnode= Node(data)
        if self.head is None:
            self.head = newnode
            return
        newnode.next= self.head
        self.head= newnode

    def printLL(self):
        if self.head is None:
            print("Linked List is empty")
            return
        currnode= self.head
        while currnode is not None:
            print(currnode.data, " ")
            currnode= currnode.next
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
            newnode.next= currnode.next
            currnode.next= newnode
        return

    def delete_element(self, data):
        if self.head is None:
            print("LinkedList is empty")
            return
        if self.head.data == data:
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

    def reverse_ll(self):
        prev = None
        currnode = self.head
        while currnode is not None:
            next= currnode.next
            currnode.next = prev
            prev = currnode
            currnode = next
        self.head = prev
        return




