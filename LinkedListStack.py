from doublyLinkedList import Node
from doublyLinkedList import DoublyLinkedList

class LinkedListStack:
    # 비어있는 양방향 리스트로 초기화
    def __init__(self):
        self.data = DoublyLinkedList()

    # 스택의 크기 반환
    def size(self):
        return self.data.getLength()

    # 스택이 비어있는지 확인
    def isEmpty(self):
        return self.size() == 0

    # 스택에 데이터 추가
    def push(self, item):
        # 노드를 새로 만듬
        node = Node(item)
        # 마지막 자리에 데이터를 넣게 된다
        self.data.insertAt(self.size() + 1, node)

    # 스택에 데이터 삭제 후 반환
    def pop(self):
        return self.data.popAt(self.size())

    # 스택의 맨 꼭대기의 데이터 반환
    def peek(self):
        return self.data.getAt(self.size()).data