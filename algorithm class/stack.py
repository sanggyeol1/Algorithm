class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    
st1 = Stack()

st1.__init__()
st1.push(1)
st1.push(2)
st1.push(3)
st1.push(4)
print(st1.size())
print(st1.pop())
print(st1.pop())
print(st1.pop())
print(st1.pop())
print(st1.size())
