class Node:
    """
    Node class

    Define every item on the linked list

    Attributes:
        value:  The item of the list in that node
        Next:   The next hope to the element to the linked list 
    """
    def __init__(self, value) -> None:
        """
        Constructore of the node
        """
        self.value = value
        # The pointer
        self.next = None



class LinkedList:
    """
    Linked List class

    Define a general class of linked list, with basic operation over the LL

    Attributes:
        lenght: The number of nodes in the LL
        head:   The first node of the LL, could be Null
        tail:   The last node of the LL, could be Null
    """
    
    def __init__(self, value) -> None:
        """
        Constructore of the LL
        """
        new_node    = Node(value = value)
        self.head   = new_node
        self.tail   = new_node
        self.length = 1

    ################################################
    #   Basic operations of Linked-List's
    ################################################
        
    def append(self, value) -> bool:
        """
        The append method add a new node to the LL
        The tail of the LL, will be the new node
        """
        new_node = Node(value = value)
        #Check if the LL is empty
        if self.length == 0:
            self.head   = new_node
            self.tail   = new_node
            self.length = 1
        else:
            #The current tail refence to the new_node
            self.tail.next  = new_node
            #The new_node is now the tail of the LL
            self.tail       = new_node
            #Increase the lenght of the LL
            self.length     += 1
        return True
    
    def pop(self) -> any:
        """
        The append method delete the last node of the LL
        The tail of the LL, will be the previus node to the tail

        Return: 
            the node poped in the LL
        """
        #Check if the LL is empty
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        #Iterate over every node of the LL until temp is None
        while(temp.next):
            prev = temp
            #Move temp to the next node
            temp = temp.next
        #Set the tail to the previus node
        self.tail       = prev
        self.tail.next  = None
        self.length     -= 1
        #If before pop the node into the LL the lenght is 0, set head and tail to None
        if self.length == 0:
            self.head = None
            self.tail = None
        #Return the pop element
        return temp
    
    def print(self) -> None:
        """
        Print every value of the nodes in the LL in ascendent order, this mean to the head until the tail
        """
        current_node = self.head
        #Iterate over every node of the LL until temp is None
        while(current_node):
            print(current_node.value)
            #Move to the next node
            current_node = current_node.next
    
    def prepend(self, value) -> bool:
        """
        Append to the the beginning of the ll a new node
        """
        new_node = Node(value=value)
        if self.length  == 0:
            self.head   =   new_node
            self.tail   =   new_node
            self.length =  1
        else:
            #Refers the new node to the LL
            new_node.next   = self.head
            #Set the head to the new node
            self.head       = new_node
            self.length     +=  1
        return True
    
    def pop_firs(self) -> any:
        """
        Delete from the ll the first element and return it

        Return
            None:   If the lenght of the ll is 0
            Any:    The value of the node
        """
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return temp.value
        
    def get(self, index) -> any:
        """
        Return the node according to the index pass to the function 
        
        Return:
            None:   If the index its out of range or is less than 0
            Any:    The value of the node  
        """
        if index < 0 or index > self.length:
            return None
        else:
            temp = self.head
            # The underscore is use to
            for _ in range(index):
                temp = temp.next
            return temp
    
    def set_value(self, index, value) -> bool:
        """
        Change the value of a node according to the index pass to the function.

        Return
            True:   If the change was succesful
            False:  If the index it's out of range or less than 0
        """
        temp = self.get(index=index)

        if temp:
            temp.value = value
            return True
        return False   

    def insert(self, index, value) -> bool:
        """
        Insert a new node in the ll according to the index pass to the function

        Return
            True:   If the insert was successful
            False:  If the index it's out of range or is less than zero
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value=value)
            return True
        elif index == self.length:
            self.append(value=value)
            return True
        else:
            new_node        = Node(value=value)
            temp            = self.get(index= index - 1)
            new_node.next   = temp.next
            temp.next       = new_node
            self.length     += 1
            return True 
    
    ################################################
    #   Common problems of Linked-List's
    ################################################

    def reverse(self) -> None:
        """
        Invert the order of the linked list

        Return
            None
        """
        temp        = self.head
        self.head   = self.tail
        self.tail   = temp
        after       = temp.next
        before      = None
        for _ in range(self.length):
            after       = temp.next
            temp.next   = before
            before      = temp
            temp        = after

    def find_middle_node(self) -> any:
        """
        Return the middle node of a linked list.
        If the linked list has an even number of nodes, 
        return the first node of the second half of the list.

        Return
            Any
        """        
        slow = self.head
        fast = self.head.next

        if self.head == None:
            return None
        
        while fast is not None:
            
            slow = slow.next
            fast = fast.next

            if fast is None:
                return slow
            
            fast = fast.next

        return slow

    def has_loop(self) -> bool:
        """
        This method detect if the linked list contain a loop 

        Return
            Bool
        """    

        slow = self.head
        fast = self.head.next

        if self.head == None:
            return False
        
        while fast is not None and fast.next is not None:
            
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
            
        return False

    def find_kth_from_end(self, k) -> any:
        """
        This method return the Kth node from the end of the linked list 

        Return
            Node
        """  
        slow = fast = self.head

        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        
        return slow
    
    def remove_duplicates(self):
        """
        This method detect if the linked list contain a loop 

        Return
            Bool
        """  
        values = set()
        previus = None
        current = self.head

        while current:
            if current.value in values:
                previus.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                previus = current
            current = current.next

    def reverse_between(self, start_index, end_index):
        """
        This method reverse elements between a start and end index 

        Return
            None
        """  

        if self.length <= 1:
            return
        
        help_node       = Node(0)
        help_node.next  = self.head
        previous_node   = help_node

        for _ in range(start_index):
            previous_node.next

        current_node = previous_node.next

        for _ in range(end_index - start_index):
            node_to_move        = current_node.next
            current_node.next   = node_to_move.next
            node_to_move.next   = previous_node.next
            previous_node.next  = node_to_move        

        self.head = help_node.next

