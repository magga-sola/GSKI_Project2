class Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    def __init__(self, element=None, next=None):
        self._element = element
        self._next = next
    def __str__(self):
        return str(self._element)


class LinkedList():
    """ A singly linked list """

    def __init__(self,head=None,next=None,tail=None):
        self._head = head
        self._tail = tail
        self._size = 0
        
    def __str__(self):
        """ Returns a string with all the items in the list, separated by a single space """
        the_str = ""

        i = self._head
        while i != None:
            the_str += str(i)
            the_str += " "
            i = i._next
        return the_str

    def isEmpty(self):
        return self._size == 0


    def push_back(self, val):

        the_node = Node(val, None)

        if self.isEmpty():
            self._head = the_node
            self._tail = the_node
        else:
            self._tail._next = the_node # this connects the last node with the new one
            self._tail = the_node # this makes the new node count as the last one

        self._size += 1


    def push_front(self,value):
        """ Takes a parameter and adds its value to the front of the list """
        the_node = Node(value,self._head)
        if not self.isEmpty():
            self._head.next = self._head
            self._head = the_node
            self._size += 1
        else:
            self._head = the_node
            self._tail = the_node

    def pop_front(self):
        """ Removes the item from the front of the list and ​returns its value """
        if not self.isEmpty():
            pop_value = self._head
            self._head = self._head._next
            self._size -= 1
            return pop_value
        else:
            return "None"

    def get_size(self):
        """ Returns the number of items currently in the list """
        return self._size

