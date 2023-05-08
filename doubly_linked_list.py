class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                nxt.prev = new_node
                new_node.prev = cur
                return
            cur = cur.next

    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prv = cur.prev
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prv
                prv.next = new_node 
                return
            cur = cur.next

    def delete(self,key):
        cur = self.head
        while cur:
            if cur == self.head and cur.data == key:
                # case 1: del head node and it is only elem
                if not cur.next:
                    cur = None
                    self.head = None
                    return

                # case 2: del head node and it is NOT only elem
                else:
                    nxt = cur.next
                    cur.next = None
                    cur = None
                    nxt.prev = None
                    self.head = nxt
                    return
            elif cur.data == key:
                # case 3: del NOT head and not last elem
                if cur.next:
                    prv = cur.prev
                    nxt = cur.next
                    prv.next = nxt
                    nxt.prev = prv
                    cur.prev = None
                    cur.next = None
                    cur = None
                    return
                # case 4: del NOT head and last elem
                else:
                    prv = cur.prev
                    prv.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next
    
    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == self.head and cur == node:
                # case 1: del head node and it is only elem
                if not cur.next:
                    cur = None
                    self.head = None
                    return

                # case 2: del head node and it is NOT only elem
                else:
                    nxt = cur.next
                    cur.next = None
                    cur = None
                    nxt.prev = None
                    self.head = nxt
                    return
            elif cur == node:
                # case 3: del NOT head and not last elem
                if cur.next:
                    prv = cur.prev
                    nxt = cur.next
                    prv.next = nxt
                    nxt.prev = prv
                    cur.prev = None
                    cur.next = None
                    cur = None
                    return
                # case 4: del NOT head and last elem
                else:
                    prv = cur.prev
                    prv.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev

    def remove_duplicates(self):
        duplicates = dict()
        if self.head is None:
            return
        else:
            cur = self.head
            while cur:
                if cur.data in duplicates:
                    nxt = cur.next
                    self.delete_node(cur)
                    cur = nxt
                else:
                    duplicates[cur.data] = 1
                    cur = cur.next
            return


    def pairs_with_sum(self, sum_val):
        answer = []
        # if sum 0 and list is empty then return empty list
        # we assume that list elements are positive
        if sum_val == 0 or self.head is None or self.head.next is None:
            return answer
        else:
            rnr = None 
            cur = self.head
            while cur:
                rnr = cur.next
                while rnr:
                    if rnr.data + cur.data == sum_val:
                        pair = "({},{})".format(cur.data, rnr.data)
                        answer.append(pair)
                    rnr = rnr.next
                cur = cur.next
            return answer
