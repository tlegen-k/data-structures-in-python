from stack import Stack

# Stack data structure implementation

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return self.items == []

    def pop(self):
        if not self.is_empty():
            self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

def convert_int_to_bin(dec_num):
    stack = Stack()
    answer = []
    while dec_num != 0:
    remainder = dec_num % 2
    stack.push(remainder)
    dec_num = dec_num // 2

    while not stack.is_empty():
    answer.append(stack.pop())
    #bin_num = ""
    #while not stack.is_empty():
    #  bin_num += str(stack.pop())
    #return bin_num
    answer_str = ''.join(map(str,answer))
    return answer_str
