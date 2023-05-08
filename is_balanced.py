# Stack data structure implementation

class Stack():
    def __init__(self):
        self.items = []
        self.length = 0

    def push(self, item):
        self.items.append(item)
        self.length += 1

    def is_empty(self):
        return self.items == []

    def pop(self):
        if not self.is_empty():
            self.length -= 1
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items
    
    def len(self):
        return self.length

def isMatch(p1, p2):
    if p1 == "[" and p2 == "]":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "(" and p2 == ")":
        return True
    else:
        return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        is_balanced = True
        index = 0

        while index < len(s) and is_balanced:
            paren = s[index]

            if paren in "([{":
                stack.push(paren)
            else:
                if stack.is_empty():
                    is_balanced = False
                    break
                else:
                    top = stack.pop()
                    if not isMatch(top,paren):
                        is_balanced = False
                        break
            index += 1
        
        if stack.is_empty() and is_balanced:
            return True
        else:
            return False

