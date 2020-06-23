class ArrayStack:
    # 빈 스택을 배열로 초기화
    def __init__(self):
        self.data = [] 
        
    # 스택의 크기
    def size(self):
        return len(self.data)
    
    # 빈 스택 판단 여부
    def isEmpty(self):
        return self.size() == 0
    
    # 데이터 원소 추가
    def push(self, item):
        self.data.append(item)
        
    # 데이터 원소 삭제 (리턴)
    def pop(self):
        return self.data.pop()
    
    # 스택의 꼭대기 원소 반환
    def peek(self):
        return self.data[-1]