class Stack(object):
    def __init__(self):
        """initialize an empty stack"""
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(object):
    def __init__(self):
        self.stack = Stack()
        self.maxes = Stack()

    def push(self, item):
        if self.maxes.peek() is None or item >= self.maxes.peek():
            self.maxes.push(item)
        self.stack.push(item)

    def pop(self):
        popped = self.stack.pop()
        if popped == self.maxes.peek():
            self.maxes.pop()
        return popped

    def peek(self):
        return self.stack.peek()

    def get_max(self):
        return self.maxes.peek()


ms = MaxStack()
ms.push(1)
print(ms.get_max())
ms.push(2)
print(ms.get_max())
ms.push(3)
print(ms.get_max())
ms.push(3)
print(ms.get_max())
ms.pop()
print(ms.get_max())
ms.pop()
ms.push(4)
print(ms.get_max())
ms.push(1)
print(ms.get_max())
