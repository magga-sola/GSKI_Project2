class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")

def reversed_list(old_node, temp_node=None):
    """ reverses a linked list """
    if old_node is not None:
        new_node = Node(old_node.data, temp_node)
        return reversed_list(old_node.next, new_node )
    else:
        return temp_node

def is_equal(ll1, ll2):
    """ checks if two linked lists are equal  """
    if ll1 is not None and ll2 is not None:
        return (ll1.data == ll2.data) and is_equal(ll1.next, ll2.next)
    return True

def palindrome(head):
    """ checks if a linked list is a palindrome """
    # creating reversed list
    reversed_ = reversed_list(head)
    # checking the two lists
    return is_equal(head,reversed_)


if __name__ == "__main__":

    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")
