class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

stack = LinkedListStack()


msg = input("문자열 입력: ")  
for c in msg:
    stack.push(c)

print("문자열 출력: ", end="") 
while not stack.isEmpty():
    print(stack.pop(), end="")