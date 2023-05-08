class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node 
            return
# iterate to reach the end
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
# assign pointer to new last element
        last_node.next = new_node

    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, node, data):
        new_node = Node(data)

        if node is None:
            return
        new_node.next = node.next
        node.next = new_node

    def delete_node(self, key):
        # first case is node to delete is head
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        # second case is node to delete is not head
        prev_node = None
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next

        # if reach the end of list then not found
        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        #same logic as with previous but use position logic instead
        if self.head:
            cur_node = self.head

            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return
            
            prev_node = None
            counter = 0
            while cur_node and counter != pos:
                prev_node = cur_node
                cur_node = cur_node.next
                counter += 1

            if cur_node is None:
                return

            prev_node.next = cur_node.next
            cur_node = None

    def len_iterative(self):
        cur_node = self.head
        counter = 0
        while cur_node:
            counter += 1
            cur_node = cur_node.next
        return counter

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        # elements are not found
        if not curr_1 or not curr_2:
            return

        # checking if element 1 is head
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        # checking if element 2 is head
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        # if none is head then just swap
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            # temp variable
            nxt = cur.next
            # actual change of poitners
            cur.next = prev
            # iteration part
            prev = cur
            cur = nxt   
        self.head = prev
    
    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)
        
    # merging by replacing original list
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        # check if lists are empty
        # if so return pointers to non-empty list
        if not p:
            return q
        if not q:
            return p

        # check first nodes 
        if p.data <= q.data:
            s = p
            p = p.next
        else:
            s = q
            q = q.next

        # store head of new list
        new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        
        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = new_head
        return self.head

    def remove_duplicates(self):
        prev = None
        cur = self.head
        duplicates = dict()

        while cur:
            if cur.data in duplicates:
                prev.next = cur.next
                cur = None
            else:
                duplicates[cur.data] = 1
                prev = cur

            cur = prev.next
    def print_nth_from_last(self, n, method):
        if method == 1:
            total_len = self.len_iterative()

            cur = self.head
            while cur:
                if total_len == n:
                    return cur.data
                cur = cur.next
                total_len -= 1

            if cur is None:
                return

        if method == 2:
            #use two pointers
            p = self.head
            q = self.head

            if n > 0:
                count = 0
                while q:
                    count += 1
                    if count >= n:
                        break
                    q = q.next

                if q is None:
                    print(f"{n} is greater than the number of nodes in the list.")

                while p and q.next:
                    p = p.next
                    q = q.next
                return p.data
            else:
                return None

    def count_occurences_iterative(self, data):
        cur = self.head
        counter = 0
        while cur:
            if cur.data == data:
                counter += 1

            cur = cur.next
        return counter

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            
            p = prev

            while q:
                prev = q
                q = q.next

            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None

    def is_palindrome_1(self):
        # method 1 using string
        cur = self.head
        s = ""
        while cur:
            s += cur.data
            cur = cur.next
        return s == s[::-1]
    # method 2 using stack analogue(array based) 
    def is_palindrome_2(self):
        p = self.head
        stack = []

        while p:
            stack.append(p.data)
            p = p.next
        
        p = self.head
        while p:
            elem = stack.pop()
            if p.data != elem:
                return false
            p = p.next
        return True

    def is_palindrome_3(self):
        if self.head:
            p = self.head
            q = self.head
            prev = []

            i = 0
            while q:
                prev.append(q)
                q = q.next
                i += 1
            q = prev[i-1]
            
            count = 1

            while count <= i//2 +1:
                if prev[-count] != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return True

    def is_palindrome(self,method):
        if method == 1:
            return self.is_palindrome_1()
        elif method == 2:
            return self.is_palindrome_2()
        elif method == 3:
            return self.is_palindrome_3()

    def move_tail_to_head(self):
        if self.head and self.head.next:
            q = self.head
            prev = None
            while q.next:
                prev = q
                q = q.next
            q.next = self.head
            self.head = q
            prev.next = None
        else:
            return

    def sum_two_lists(self, llist):
        # get numbers in each list and store in stack (as orders reversed)
        # create new linked list and push values from stack
        if self.head and llist.head:
            p = self.head
            q = llist.head

            new_llist = LinkedList()

            sum = 0
            remainder = 0
            extra = 0
            # we assume that feed linked lists have same length
            # and sum does not require additional digit
            while p or q:
                if not p:
                    i = 0
                else:
                    i = p.data
                if not q:
                    j = 0
                else:
                    j = q.data
                sum = i + j + extra

                if sum >= 10:
                    remainder = sum - 10
                    extra = 1
                else:
                    remainder = sum
                    extra = 0
                new_llist.append(remainder)
                if p:
                    p = p.next
                if q:
                    q = q.next
            return new_llist
        else:
            if not self.head:
                return llist
            else:
                return self

        # solution using strings
#            num_1 = ""
#            while p:
#                num_1 += str(p.data)
#                p = p.next
#            num_1_corr = num_1[::-1]
#
#            num_2 = ""
#            while q:
#                num_2 += str(q.data)
#                q = q.next
#            num_2_corr = num_2[::-1]
#
#            sum_int = int(num_1_corr) + int(num_2_corr)
#
#            new_llist = LinkedList()
#
#            for item in reversed(str(sum_int)):
#                new_llist.append(item)
#            return new_llist


