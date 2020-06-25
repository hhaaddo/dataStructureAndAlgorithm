from doublyLinkedList import Node, DoublyLinkedList

# 배열로 구현한 큐
class ArrayQueue:
    # 빈 큐를 초기화
    def __init__(self):
        self.data = []
        
    # 큐의 크기를 리턴
    def size(self):
        return len(self.data)

    # 큐가 비어있는지 판단
    def isEmpty(self):
        return self.size() == 0
    
    # 데이터 원소 추가 연산
    def enqueue(self, item):
        self.data.append(item)
        
    # 데이터 원소 삭제 연산
    def dequeue(self):
        return self.data.pop(0)
    
    # 큐의 맨 앞 원소 반환
    def peek(self):
        return self.data[0]




# 연결 리스트로 구현한 큐
class LinkedListQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.nodeCount

    def isEmpty(self):
        return self.data.nodeCount==0

    def enqueue(self, item):
        node = Node(item)
        self.data.insertAt(self.size()+1,node)

    def dequeue(self):
        return self.data.popAt(1)

    def peek(self):
        return self.data.head.next.data



# 환형 큐
class CircularQueue:
    # 빈 큐를 초기화 (주어진 인자로 큐의 최대) 길이 설정
    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1
        
    # 현재 큐 길이를 반환
    def size(self):
        return self.count
    
    # 큐가 비어있는가?
    def isEmpty(self):
        return self.count == 0
    
    # 큐가 꽉 차있는가?
    def isFull(self):
        return self.count == self.maxCount
    



    # 정해진 공간을 빙 돌려가며 이용, 즉 공간을 재활용해야 하기 때문에, 
    # front 와 rear 를 마냥 증가시키기만 함으로써는 환형 큐를 구성할 수 없다. 
    # 문제 해결 방법!!!! 환형은 나머지를 이용하자!!!

    # 큐에 데이터 원소 추가
    def enqueue(self, x):
        if self.isFull():
            # IndexError('Queue full') exception으로 처리
            pass
        
        self.rear = (self.rear + 1) % self.maxCount
        self.data[self.rear] = x
        self.count += 1

    # 큐에서 데이터 원소 뽑아내기
    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue empty')

        self.front = (self.front + 1) % self.maxCount
        x = self.data[self.front]
        self.count -= 1
        return x

    # 큐의 맨 앞 원소 들여다 보기
    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front + 1) % self.maxCount]



# 우선순위 큐
class PriorityQueue:
    # 양방향 연결리스트를 이용하여 빈 큐를 초기화
    def __init__(self, x):
        self.queue = DoublyLinkedList()
    
    # 크기를 반환
    def size(self):
        return self.queue.getLength()

    # 비어있는가?
    def isEmpty(self):
        return self.size() == 0
        
    # 데이터 삽입 연산
    def enqueue(self, x):
        newNode = Node(x)
        
        # 처음 시작하는 위치 head에서 시작
        curr = self.queue.head
        
        # 끝까지 가지 않을 조건 && 우선순위를 비교하는 조건
        while curr.next != self.queue.tail and x < curr.next.data :
            curr = curr.next
        
        # 양방향 연결리스트를 이용해 삽입! 
        self.queue.insertAfter(curr, newNode)
        
        # [주의] 양방향 연결리스트의 getAt()메서드를 이용하지 않는다.
        # why? 
    
    # 데이터 삭제 연산
    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())

    # 첫번째 데이터 반환
    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data