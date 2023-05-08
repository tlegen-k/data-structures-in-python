class Queue(object):
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    # we assume that last element to be front of the queue
    # and the first element is the back of the queue
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)



