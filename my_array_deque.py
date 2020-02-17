
class ArrayDeque():
    def __init__(self):
        self.size = 0
        self.capacity = 5
        self.arr = [0] * self.capacity
        self.start_index =  0

    def __str__(self):
        """ Returns a string with all the items in the deque, separated by a single space """
        return_string = ""
        for i in range(self.size):
            return_string += str(self.arr[i]) + " "
        return return_string

    def resize(self):
        temp_list = [0] * (2*self.capacity)
        for i in range(self.size):
            temp_list[i] = self.arr[i]
        self.arr = temp_list
        self.capacity *= 2

    def push_back(self,value):
        """ Takes a parameter and adds its value to the back of the deque """
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = value
        self.size += 1

    def push_front(self, value):
        """ Takes a parameter and adds its value to the front of the deque """
        if self.size == self.capacity:
            self.resize()
        for i in range(self.size):
            self.arr[self.size - i] = self.arr[self.size - (i+1)]

        self.arr[0] = value
        self.size += 1

    def pop_back(self):
        """ Removes the item from the back of the deque and returns its value """
        #if empty return None
        if self.size == 0:
            return None
        else:
            self.arr[self.size] = self.arr[self.size - 1]
            self.size -= 1
            return self.arr[self.size]

    def pop_front(self):
        """ Removes the item from the front of the deque and returns its value """
        #if empty return None
        if self.size == 0:
            return None
        else:
            self.arr[0] = self.arr[1]
            self.size -= 1
            return self.arr[0]

    def get_size(self):
        """ Returns the number of items currently in the deque """
        return self.size

deque = ArrayDeque()

deque.push_back(4)
deque.push_back(5)
deque.push_back(9)
deque.push_front(9)
print(deque)
print(deque.pop_back())
print(deque.pop_back())
print(deque.pop_front())
print(deque)

print(deque.get_size())