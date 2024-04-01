class Node:
    def __init__(self, value: any) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value: any) -> None:
        new_node = Node(value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    def print_list(self) -> None:
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value: any):
        """
        It adds a new node containing a specified value to the end of a doubly linked list

        Args
            Value: the data that will contain the new node
        Return
            None
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next  = new_node
            new_node.prev   = self.tail
            self.tail       = new_node
        self.length += 1
    
    def pop(self) -> any:
        """
        This method removes and returns the last element from a doubly linked list.

        Return
            None: if the doubly linked list is empty
            Node: if the doubly linked list is not empty
        """
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
        
    def prepend(self, value: any) -> bool:
        """
        This method adds a new node containing a specified value to the beginning (front) of a doubly linked list
        
        Args
            Value: the data that will contain the new node
        Return
            bool
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True