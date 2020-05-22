class Queue(object):
    def __init__(self):
        """initialize an empty queue"""
        self.input_stack = []
        self.output_stack = []

    def enqueue(self, item):
        self.input_stack.append(item)

    def dequeue(self):
        if len(self.output_stack) == 0 and len(self.input_stack) == 0:
            return None
        if len(self.output_stack):
            return self.output_stack.pop()
        else:
            self._shift()
            return self.output_stack.pop()
        return

    def peek(self):
        if len(self.output_stack) == 0 and len(self.input_stack) == 0:
            return None
        if len(self.output_stack):
            return self.output_stack[len(self.output_stack)-1]
        else:
            self._shift()
            return self.output_stack[len(self.output_stack)-1]

    def _shift(self):
        while len(self.input_stack):
            self.output_stack.append(self.input_stack.pop())


q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.peek())
print(q.dequeue())
print(q.peek())
q.enqueue(3)
print(q.peek())
print(q.dequeue())
print(q.dequeue())
print(q.peek())
