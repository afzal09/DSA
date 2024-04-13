class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def append(self,data):
        new_Node = Node(data)
        new_Node.next = self.tail
        new_Node.prev = self.tail.prev
        self.tail.prev.next = new_Node
        self.tail.prev = new_Node

    def prepend(self, data):
        new_Node = Node(data)
        new_Node.next = self.head.next
        new_Node.prev = self.head
        self.head.next.prev = new_Node
        self.head.next = new_Node
    
    def delete(self, key):
        current = self.head.next
        while current != self.tail:
            if current.data == key:
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            current = current.next

    def printlist(self):
        current = self.head.next
        while current != self.tail:
            print(current.data)
            current = current.next
            

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.prepend(0)
dll.printlist()
print("\n")
dll.delete(5)
dll.delete(4)
dll.delete(2)
dll.delete(0)
dll.printlist()