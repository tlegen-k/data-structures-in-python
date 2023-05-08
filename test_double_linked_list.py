from doubly_linked_list import DoublyLinkedList

# Test cases for implementation
    
dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)

dllist.print_list()

del(dllist)
print("Test add after and add before")
dllist = DoublyLinkedList()

dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)
dllist.add_after_node(3,6)
dllist.add_before_node(4,9)

dllist.print_list()
del(dllist)
print("Test add for delete")
dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

dllist.delete(1)
dllist.delete(6)
dllist.delete(4)

dllist.delete(3)
dllist.print_list()
del(dllist)
print("Test reversal")
dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.reverse()
dllist.print_list()
