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
    
    def pop_first(self) -> any:

        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index) -> any:

        if index < 0 or index >= self.length:
            return None
        if index < self.length/2 :
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index,-1):
                temp = temp.prev
        return temp
    
    def set(self, index: int, value: any) -> bool:
        
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index: int, value: any) -> bool:
        

        if index >= self.length or index < 0:
            return False
        if self.length == 0 or self.length == index:
            self.append(value)
        else:
            before = self.get(index - 1)
            after = self.get(index)

            new_node = Node(value)
            
            new_node.prev = new_node
            new_node.next = after
            
            before.next = new_node
            after.prev = new_node

            self.length += 1 
        
        return True
    
    def remove(self, index: int) -> any:

        if index >= self.length or index < 0:
            return False
        if self.length == 0 or self.length == index:
            self.append(value)
        else:
            pass





















