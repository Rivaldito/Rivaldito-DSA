from linkedList import LinkedList

if __name__ == "__main__":
    
    #Test the constructor
    ll = LinkedList("Hey")
    #Test the append method
    ll.append("Hi")
    ll.append("Its me")
    ll.append("last node")
    # #Test Print method
    # print("################")
    # ll.print()
    # #Test the pop method
    # print("################")
    # print(ll.pop().value)
    # print("################")
    # ll.print()

    ll.insert(0,"test")
    ll.print()