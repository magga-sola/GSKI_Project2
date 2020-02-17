from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:
    def __init__(self,_type=""):
        self._type = _type
        if _type == "array":
            self.container = ArrayDeque()
        elif _type == "linked":
            self.container = LinkedList()

    def add(self,value):
        """ Takes a parameter and adds its value to the back of the queue """
        self.container.push_back(value)

    def remove(self):
        """ Removes the item off the front of the queue and ​returns ​its value, If the queue is empty, return None"""
        return self.container.pop_front()

    def get_size(self):
        """ Returns the number of items currently in the queue """
        return self.container.get_size()


"""
The class should own (as an instance variable) an instance of A​rrayDeque ​
or ​LinkedList ​and implement its own operations ​only w​ith forwarding calls 
to the operations of the encapsulated container.


The class ​Queue​ should take ​type ​as a parameter 
in its constructor. ​type​ is a string, and if it equals “array” 
it uses the ​ArrayDeque a​ s a container, if type equals “linked” it 
should use LinkedList​.
"""