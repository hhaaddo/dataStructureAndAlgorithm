from linkedList import Node

# LinkedList 클래스
class DummyLinkedList:
    ## 생성자 ##
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail


    ## 리스트 순회 ##
    def traverse(self):
        result = []
        curr = self.head
        # 현재 노드의 next가 존재하는 동안 반복
        while curr.next:
            result.append(curr.data)
            curr = curr.next
        return result

    
    ## 특정 원소 참조 ##
    def getAt(self, pos):
        # 더미노드가 추가되었으니 0미만이거나 노드개수보다 많으면 에러 (getAt(0) -> head)
        if pos < 0 or pos > self.nodeCount:
            return None
        
        i = 0 # 더미노드가 추가되었으니 0부터 시작
        curr = self.head # 연결리스트의 첫번째 노드를 가르킴
        
        # i가 pos보다 작은 동안에 i를 하나씩 증가시키면서 curr를 curr의 next를 가르키게 한다
        while i < pos: 
            curr = curr.next
            i += 1
        
        return curr


    ## 원소의 삽입 ##
    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        # 맨 뒤에 삽입을 하는 경우라면 tail도 조정해줘야함
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True


    ## 원소의 삽입 ##
    def insertAt(self, pos, newNode):
        # 범위 유효성 확인
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        
        # pos 가 1일때는 빈 공간에 삽입하는 경우니까 tail을 넣어주면 안된다. 
        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        
        else:
            prev = self.getAt(pos-1)
        
        return self.insertAfter(prev, newNode)


    ## 원소의 삭제 ##
    def popAfter(self, prev):
        # prev다음에 노드가 없는 경우 삭제할 노드가 없으니 None 리턴
        if prev.next == None:
            return None
            
        # 삭제하려는 노드를 curr에 담기
        curr = prev.next
        
        # 삭제할 노드가 없는 경우
        if curr.next == None:
            # 유일한 노드일 때
            if self.nodeCount == 1:
                self.tail = None
            # 유일한 노드가 아닐 때
            else:
                self.tail = prev
        
        # 링크 조정
        prev.next = curr.next
        self.nodeCount -= 1
        return curr.data

    
    ## 원소의 삭제 ##
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        prev = self.getAt(pos-1)
        return self.popAfter(prev)


    ## 두 리스트의 연결 ##
    def concat(self, L):
        # 원래 리스트의 맨 끝이 이어붙이려는 리스트의 처음으로
        self.tail.next = L.head.next
        # 리스트 L이 비어있을 경우
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount