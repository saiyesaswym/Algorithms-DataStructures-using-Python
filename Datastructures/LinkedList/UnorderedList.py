"""
Unordered List is built from a collection of nodes, each node linked to next
Each list object will maintain a single reference to the head of the list
List class does not contain any node objects, only a reference to the first node
Reference to NONE denotes the end of list
"""

from LinkedList import Node

class unorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def insert_at_start(self, item):
        """
        New node is added at the head of list
        Create a new node object and assign existing head as next to it
        Modify the head of list to refer to new node
        """
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def insert_at_end(self, item):
        """
        Insert new node at the end of list
        """
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            return
        else:
            n = self.head
            while n.getNext() is not None:
                n = n.getNext()
            n.setNext(new_node)

    def length(self):
        """
        Traverse the list and keep a count of number of nodes
        """
        current = self.head
        count=0
        while current!=None:
            count+=1
            current = current.getNext()

        return count

    def search(self, item):
        """
        Traverse the list and look for the item until it's found
        """
        current = self.head
        found = False
        while current!=None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def traverse(self):
        """
        Traverse the list and print all the items
        """
        if self.head is None:
            print("List has no elements")
            return
        else:
            n = self.head
            while n is not None:
                print(n.getData())
                n = n.getNext()

    def remove(self, item):
        """
        Traverse the list, look for the item
        If found, link the previous node to next node, skipping the current
        """
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def reverse(self):
        """
        Traverse through the list and reverse the assignment using three variables
        n -> current
        prev -> previous node
        next -> next node
        """
        prev = None
        n = self.head
        while n is not None:
            next = n.getNext()
            n.setNext(prev)
            prev = n
            n = next
        self.head = prev
