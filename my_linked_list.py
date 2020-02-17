
class LinkedList():
    """ A singly linked list """
    class Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        def __init__(self, element, next):
            self. element = element
            self. next = next

    def __init__(self,head=None,next=None):
        self._head = head
        self._next = next
        self._size = 0
        
    def __str__(self):
        """ Returns a string with all the items in the list, separated by a single space """
        pass

    def push_back(self):
        """ Takes a parameter and adds its value to the back of the list """
        pass
    def push_front(self):
        """ Takes a parameter and adds its value to the front of the list """
        pass
    def pop_front(self):
        """ Removes the item from the front of the list and ​returns its value """
        pass
    def get_size(self):
        """ Returns the number of items currently in the list """
        pass