# 1.(원형 큐) : 클래스 정의 와 생성자 
class ArrayQueue:
    def __init__(self, capacity=10):    
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0
        
    # 2.(원형 큐) : 공백 상태와 포화 상태 검사
    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear+1)%self.capacity  
    
    # 3.(원형 큐) : 삽입 연산
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1)%self.capacity # 후단 회전
            self.array[self.rear] = item
        else:
            print('stack overflow!')
            pass
        
    # 4.(원형 큐) : 삭제 연산
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%self.capacity  # 전단 회전
            return self.array[self.front]
        
    # 5. (원형 큐) : 상단 참조 연산
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front+1)%self.capacity]
        else: pass
        
    # 6. (원형 큐) : 전체 요소 수
    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    
    # 7. (원형 큐) : 전체 요소 화면에 출력
    def display(self, msg='Queue: '):
        print(msg, end='=[')
        count = self.size()
        for i in range(count):
            print(self.array[(self.front+1+i)%self.capacity], end=' ')
        print("]")
        
        
        
import random
q = ArrayQueue(8)                    # 큐 객체를 생성(capacity=8)

q.display("초기 상태")
while not q.isFull() :               # 큐에 빈 칸인 남았으면
    q.enqueue(random.randint(0,100)) # 0~99사이의 정수 발생->삽입
q.display("포화 상태")

print("삭제 순서: ", end='') 
while not q.isEmpty() :             # 큐에 요소가 남아 있으면
    print(q.dequeue(), end=' ')     # 꺼내서 화면에 출력
print()