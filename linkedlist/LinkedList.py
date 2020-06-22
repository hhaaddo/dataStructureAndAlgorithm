# LinkedList 클래스
class LinkedList:
    ## 생성자 ##
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    ## 특정 원소 참조 ##
    def getAt(self, pos):
        # 특정위치가 0보다 작거나 노드의 길이보다 크면 None을 반환
        if pos <= 0 or pos > self.nodeCount:
            return None
        
        i = 1
        curr = self.head # 연결리스트의 첫번째 노드를 가르킴
        
        # i가 pos보다 작은 동안에 i를 하나씩 증가시키면서 curr를 curr의 next를 가르키게 한다
        # 즉 pos-1번 만큼 전진하면 그때 curr가 가르키는 것이 내가 리턴하려는 pos번째 노드가 된다
        while i < pos: 
            curr = curr.next
            i += 1
        
        return curr


    ## 리스트 순회 ##
    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

    
    ## 길이 얻어내기 ##
    def getLength(self):
        return self.nodeCount


    ## 원소의 삽입 ##
    def insertAt(self, pos, newNode):
        # pos의 위치가 유효한지 확인
        if pos < 1 or pos > self.nodeCount + 1 :
            # pos위치가 삽입할 수 있는 범위 밖에 있을 때 False 반환
            return False
        
        # 노드를 맨 처음 위치에 삽일할 때(prev없음)
        if pos == 1: # (빈 노드의 삽입할 조건에 걸림)
            newNode.next = self.head # 새로운 노드의 next는 head
            self.head = newNode # 헤드가 새로운노드가 된다
        
        # 삽입하려는 위치가 처음이 아닐 때
        else: 
            if pos == self.nodeCount + 1: # 삽입하려는 위치가 맨끝일 때
                prev = self.tail # prev == tail과 같음(앞에서 부터 찾을 필요 없음)
            else: # 삽입하려는 위치가 처음도 아니고 맨끝도 아닐 때
                prev = self.getAt(pos-1) # 끼워넣으려는 직전의 위치를 얻어낸다
            
            newNode.next = prev.next # 새로운 노드가 prev.next를 가르키도록한다.
            prev.next = newNode # prev.next를 newNode로 한다
        
        # 맨 마지막 위치에 삽입 할 때 (빈 노드의 삽입할 조건에 걸림)
        if pos == self.nodeCount + 1:
            self.tail = newNode # Tail을 새로운 노드로 변경
            
        # 마지막으로 노드의 갯수 증가
        self.nodeCount += 1
        return True


    ## 원소의 삭제 ##
    def popAt(self, pos):
        # pop 값이 유효한지 확인 적당한 값이 아닐 경우 에러발생
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
            
        # 맨 앞의 노드를 삭제하는 경우
        if pos == 1:
            curr = self.head
            self.head = self.getAt(pos+1)
            
            # 유일한 노드인 경우
            if self.nodeCount == 1:
                self.tail = None
                self.head = None
        
        # 맨 앞의 노드가 아닐 때
        else:
            prev = self.getAt(pos-1)
            curr = self.getAt(pos)
            prev.next = curr.next
            
            # 맨 끝 노드일 때
            if pos == self.nodeCount:
                self.tail = prev
                
        r = curr.data
        self.nodeCount -= 1
        
        return r


    ## 두 리스트의 연결 ##
    def concat(self, L):
        # 원래 리스트의 맨 끝이 이어붙이려는 리스트의 처음으로
        self.tail.next = L.head
        
        # L.tail이 none인 경우 실행 안됨
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount