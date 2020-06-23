from node import DoublyNode

# 양방향 연결 리스트 클래스
class DoublyLinkedList:
    ## 생성자 ##
    def __init__(self, item):
        self.nodeCount = 0
        self.head = DoublyNode(None)
        self.tail = DoublyNode(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    ## 리스트 순회 ##
    def traverse(self):
        result = []
        curr = self.head
        
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
            
        return result


    ## 리스트 역순회 ##
    def reverse(self):
        result = []
        curr = self.tail
        
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
            
        return result


    ## 원소의 삽입 ##
    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    ## 특정 원소 얻어내기 ##
    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None
        
        # pos가 오른쪽으로 치우쳐있는 경우 tail쪽에서 계산
        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail

            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        
        # pos가 왼쪽으로 치우쳐 있는 경우 head에서 계산
        else:
            i = 0
            curr = self.head
            
            while i < pos:
       	        curr = curr.next
                i += 1

        return curr


    ## 원소의 삽입 ##
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        
        prev = self.getAt(pos-1)
        return self.insertAfter(prev, newNode)


    ## 원소의 삭제 ##
    def popAfter(self, prev):
        curr = prev.next
        
        prev.next = curr.next
        curr.next.prev = prev
        
        self.nodeCount -= 1
        
        return curr.data
    
    def popBefore(self, next):
        curr = next.prev
        
        next.prev = curr.prev
        curr.prev.next = next
        
        self.nodeCount -= 1
        
        return curr.data
    
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        
        prev = self.getAt(pos-1)
        return self.popAfter(prev)


    ## 두 리스트의 병합 ##
    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        
        self.tail = L.tail
        self.nodeCount += L.nodeCount