
class ArrayDeque():
    def __init__(self):
        self.size = 0
        self.capacity = 5
        self.arr = [0] * self.capacity

    def __str__(self):
        """ Returns a string with all the items in the deque, separated by a single space """
        return_string = ""
        for i in range(self.size):
            return_string += str(self.arr[i]) + ", "
        return return_string

    def resize(self):
        temp_list = [0] * (2*self.capacity)
        for i in range(self.size):
            temp_list[i] = self.arr[i]
        self.arr = temp_list
        self.capacity *= 2

    def push_back(self,value):
        """ Takes a parameter and adds its value to the back of the deque """
        pass

    def push_front(self):
        """ Takes a parameter and adds its value to the front of the deque """
        pass

    def pop_back(self):
        """ Removes the item from the back of the deque and returns its value """
        #if empty return None
        pass

    def pop_front(self):
        """ Removes the item from the front of the deque and returns its value """
        #if empty return None
        pass

    def get_size(self):
        """ Returns the number of items currently in the deque """
        pass