
class LinkedList():
    """ A singly linked list """
    class Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self,head=None,next=None):
        self._head = head
        self._next = next
        self._size = 0
        
    def __str__(self):
        """ Returns a string with all the items in the list, separated by a single space """
        the_str = ""
        if not self.isEmpty():
            the_str += str(self._head)
            self._head = self._next
        return the_str

    def isEmpty(self):
        return self._size == 0

    def push_back(self,value):
        """ Takes a parameter and adds its value to the back of the list """
        value_node = self.Node(value,None)
        self._size += 1
        if self.isEmpty():
            self._head = value_node
        else:
            self._next = value_node

    def push_front(self,value):
        """ Takes a parameter and adds its value to the front of the list """
        if not self.isEmpty():
            value_node = self.Node(value,self._head)
            self._head = value_node
            self._size += 1
        else:
            print("it's empty yo")

    def pop_front(self):
        """ Removes the item from the front of the list and ​returns its value """
        if not self.isEmpty():
            #answer = self._head #answer
            self._head = self._next
            self._size -= 1
            return self._head
        else:
            return "this is empty"

    def get_size(self):
        """ Returns the number of items currently in the list """
        return self._size


print("\nTESTING LINKED_LIST\n")

lis = LinkedList()
lis.push_back(3)
lis.push_back(1)
lis.push_back(6)
lis.push_back(9)
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_front())
print(lis.pop_front())
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
lis.push_front(11)
lis.push_front(16)
lis.push_front(13)
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_front())
print(lis.pop_front())
print(lis.pop_front())
print(lis.pop_front())
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_front())
print(lis.pop_front())
print("container of size: " + str(lis.get_size()) + ":")
print(lis)