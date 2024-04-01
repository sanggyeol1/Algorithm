import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedQueue:
    def __init__(self):
        self.rear = None
        
    def isEmpty(self):
        return self.rear == None

    def enqueue(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.rear = newNode
            newNode.next = newNode
        else:
            newNode.next = self.rear.next
            self.rear.next = newNode
            self.rear = newNode

    def dequeue(self):
        if self.isEmpty():
            print('Queue is empty')
            return None
        else:
            if self.rear.next == self.rear:
                data = self.rear.data
                self.rear = None
            else:
                data = self.rear.next.data
                self.rear.next = self.rear.next.next
            return data

    def peek(self):
        if self.isEmpty():
            print('Queue is empty')
            return None
        else:
            return self.rear.next.data

    def size(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            current = self.rear.next
            while current != self.rear:
                count += 1
                current = current.next
            return count

    def display(self, msg='Queue: '):
        print(msg, end='[')
        if not self.isEmpty():
            current = self.rear.next
            while True:
                print(current.data, end=' ')
                current = current.next
                if current == self.rear.next:
                    break
        print("]")

q = CircularLinkedQueue()
q.display("초기 상태")
for _ in range(8):
    q.enqueue(random.randint(0,100))
q.display("포화 상태")
print("삭제 순서: ", end='') 
while not q.isEmpty():
    print(q.dequeue(), end=' ')
print()
