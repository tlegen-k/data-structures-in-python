class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def remove(self,key):
        # assume no duplicate elements
        # i.e. deleting first occurence
        
        if self.head:
            if self.head.data == key:
                # if only element
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur = self.head
                    while cur.next != self.head:
                        cur = cur.next
                    cur.next = self.head.next
                    self.head = self.head.next

            else:
                cur = self.head
                prev = None
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next
                        cur = cur.next

    def remove_node(self, node):
        # assume no duplicate elements
        # i.e. deleting first occurence
        
        if self.head:
            if self.head == node:
                # if only element
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur = self.head
                    while cur.next != self.head:
                        cur = cur.next
                    cur.next = self.head.next
                    self.head = self.head.next

            else:
                cur = self.head
                prev = None
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next
                    if cur == node:
                        prev.next = cur.next
                        cur = cur.next
    def __len__(self):
        count = 0
        cur = self.head
        while cur:
            cur = cur.next
            count += 1
            if cur == self.head:
                break
        return count

    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size//2
        count = 0

        prev = None
        cur = self.head
        # split off first half
        while cur and count < mid:
            prev = cur
            cur = cur.next
            count += 1
        prev.next = self.head

        # creating new second half
        other = CircularLinkedList()
        while cur != self.head:
            other.append(cur.data)
            cur = cur.next
        self.print_list()
        print("\n")
        other.print_list()

    def josephus_circle(self, step):
        # each step-th person is killed
        length = len(self)
        cur = self.head
        while length > 1:
            count = 1
            while count != step:
                count += 1
                cur = cur.next
            print(f"Kill {cur.data}")
            self.remove_node(cur)
            cur = cur.next
            length -= 1

    def is_circular_linked_list(self):
        cur = self.head
        # if empty
        if cur is None:
            return False
        # otherwise need to reach the end of list
        # if it points to the head of list then true
        while cur and cur.next != self.head and cur.next != None:
            cur = cur.next
            print(f"cur={cur.data}")
        if cur.next == self.head:
            return True
        else:
            return False
