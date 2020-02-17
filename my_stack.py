from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack:
    def __init__(self, type=""):
        self._type = type
        self._size = 0
        self.AD_instance = ArrayDeque()
        self.LL_instance = LinkedList()

    def __str__(self):
        the_str = ""
        return the_str

    def push(self):
        """ Takes a parameter and adds its value onto the stack """
        pass

    def pop(self):
        """ Removes the item off the top of the stack and ​returns ​its value. if stack is empty returns None"""
        pass

    def get_size(self):
        """ Returns the number of items currently on the stack """
        return self._size

"""
The class should own (as an instance variable) an instance of A​rrayDeque ​
or ​LinkedList ​and implement its own operations ​only w​ith forwarding calls 
to the operations of the encapsulated container.


The class ​Stack s​hould take ​type ​as a parameter 
in its constructor.
 ​type ​is a string, and if it equals “array” it uses the ​ArrayDeque ​as a container, 
 if type equals “linked” it should use LinkedList​.
"""