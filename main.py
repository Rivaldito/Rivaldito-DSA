from linkedList import LinkedList
from doubleLinkedList import DoublyLinkedList

if __name__ == "__main__":
    
    dll = DoublyLinkedList("🔥")
    dll.append("⛱️")
    dll.append("🌊")
    dll.print_list()
    dll.pop()
    dll.print_list()
    dll.prepend("🏝️")
    dll.print_list()