class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*capacity
        self.top = -1
        
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity
    
    def push(self, item):
        if not self.isFull():
            self.top+=1
            self.array[self.top] = item
        else:
            print("stack overflow")
            pass
    
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else:
            print("stack underflow")
            pass
    
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            pass
        
    def size(self):
        return self.top+1
    
    

stack = ArrayStack(100)

msg = input("문자열입력 : ")
for c in msg:
    stack.push(c)
    
print("문자열 출력 : ", end="")
while not stack.isEmpty():
    print(stack.pop(), end="")