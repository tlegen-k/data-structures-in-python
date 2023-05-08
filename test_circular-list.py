from circular_list import CircularLinkedList

# tests
cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.print_list()
cllist.prepend("B")
cllist.prepend("A")
cllist.print_list()

cllist.remove("A")
cllist.print_list()
cllist.remove("D")
cllist.print_list()

del(cllist)

cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.append("E")
cllist.append("F")
cllist.append("G")
cllist.append("H")

cllist.split_list()
del(cllist)
print("Joseph's circle")
cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)
cllist.append(5)
cllist.append(6)


cllist.josephus_circle(2)
cllist.print_list()

del (cllist)
cllist = CircularLinkedList()
cllist.append(1)
print(cllist.is_circular_linked_list())
