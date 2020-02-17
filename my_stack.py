from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack:
    def __init__(self, _type=""):
        self._type = _type # if type == array then use AD_instance, elif type == linked then use LL_instance
        if _type == "array":
            self.container = ArrayDeque()
        elif _type == "linked":
            self.container = LinkedList()

    def push(self,value):
        """ Takes a parameter and adds its value onto the stack """
        self.container.push_back(value)

    def pop(self):
        """ Removes the item off the top of the stack and ​returns ​its value. if stack is empty returns None"""
        return self.container.pop_front()

    def get_size(self):
        """ Returns the number of items currently on the stack """
        return self.container.get_size()


"""
The class should own (as an instance variable) an instance of A​rrayDeque ​
or ​LinkedList ​and implement its own operations ​only w​ith forwarding calls 
to the operations of the encapsulated container.


The class ​Stack s​hould take ​type ​as a parameter 
in its constructor.
 ​type ​is a string, and if it equals “array” it uses the ​ArrayDeque ​as a container, 
 if type equals “linked” it should use LinkedList​.
"""

###### TESTS #######

"""
print("\nTESTING STACK WITH ARRAYS\n")

stack = Stack("array")
stack.push(2)
stack.push(4)
stack.push(7)
print("the data structure is of size: " + str(stack.get_size()))
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("the data structure is of size: " + str(stack.get_size()))
"""

print("\nTESTING STACK WITH LINKED_LIST\n")

stack = Stack("linked")
stack.push(2)
stack.push(4)
stack.push(7)
print("the data structure is of size: " + str(stack.get_size()))
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("the data structure is of size: " + str(stack.get_size()))
