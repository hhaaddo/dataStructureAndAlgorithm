# 이진 탐색 트리

# 노드 클래스
class Node:
    # 초기화
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    # 이번에는 노드들의 리스트를 만들어서 리턴한다.
    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self

    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self

    # parent 인자가 주어지지않으면 None으로 생각하라는 말
    def lookup(self, key, parent=None):
        # 지금 방문된 노드(self.key)보다 탐색하려는 키가 작으면 왼쪽으로 가야함
        if key < self.key:
            # 왼쪽 자식이 있을 때
            if self.left:
                # 재귀적으로 호출
                return self.left.lookup(key, self)
            else:
                # 찾으려는 키가 없구나
                return None, None
        
        # 지금 방문된 노드보다 찾으려는 키가 크면 오른쪽으로 가야함
        elif key > self.key:
            # 오른쪽 자식이 있을 때
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        
        # 찾았다 해당 노드!
        else:
            return self, parent

    def insert(self, key, data):
        # 찾으려는 키가 해당노드보다 작은 경우 왼쪽으로
        if key < self.key:
            # 왼쪽 자식 노드가 존재하는 경우
            if self.left:
                self.left.insert(key, data)
            # 존재하지않으면 노드를 단다.
            else:
                self.left = Node(key, data)
                
        # 찾으려는 키가 해당 노드보다 큰 경우 오른쪽으로        
        elif key > self.key:
            # 오른쪽 자식 노드가 존재하는 경우 
            if self.right:
                self.right.insert(key, data)
            # 존재하지 않으면 노드를 단다.
            else:
                self.right = Node(key, data)
                
        # 중복된 노드가 존재하는 경우 에러 발생
        else:
            raise KeyError('Key %s already exists.' % key)

        return True

    # 자식을 세어보자
    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count
    

    
# 이진 탐색 트리 클래스
class BinSearchTree:
    # 저번에는 인자를 주었는데 이번에는 none으로 초기화
    def __init__(self):
        self.root = None
    
    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def min(self):
        # 루트 노드가 존재하면
        if self.root:
            return self.root.min()
        else:
            return None

    def max(self):
        if self.root:
            return self.root.max()
        else:
            return None

    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None

    # 노드 삽입
    def insert(self, key, data):
        # 존재하는 트리라면
        if self.root:
            self.root.insert(key,data)
        
        # 트리가 존재하지않다면 해당 노드를 루트에 넣는다.
        else:
            self.root = Node(key, data)

    # 노드 삭제
    def remove(self, key):
        # 삭제하려는 노드와 p를 검색
        node, parent = self.lookup(key)

        # 삭제하려는 노드가 존재하면
        if node:
            # 자식노드의 개수가 몇개 있는지 확인
            nChildren = node.countChildren()

            # The simplest case of no children
            if nChildren == 0:
                # 만약 parent 가 있으면 (루트노드가 아니란소리)
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # parent.left 또는 parent.right 를 None 으로 하여
                # leaf node 였던 자식을 트리에서 끊어내어 없앱니다.
                if parent:
                    if parent.left == node:
                        parent.left = None
                    if parent.right == node:
                        parent.right = None

                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 를 None 으로 하여 빈 트리로 만듭니다.
                else:
                    self.root = None


            # When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                # 그 자식을 어떤 변수가 가리키도록 합니다.
                if node.left:
                    temp = node.left
                else:
                    temp = node.right

                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node 의 자리에 넣습니다.
                if parent:
                    if parent.left == node:
                        parent.left = temp
                    else:
                        parent.right = temp
                
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 에 위에서 가리킨 자식을 대신 넣습니다.
                else:
                    self.root = temp
            
            # When the node has both left and right children
            else:
                parent = node
                successor = node.right
                # parent 는 node 를 가리키고 있고,
                # successor 는 node 의 오른쪽 자식을 가리키고 있으므로
                # successor 로부터 왼쪽 자식의 링크를 반복하여 따라감으로써
                # 순환문이 종료할 때 successor 는 바로 다음 키를 가진 노드를,
                # 그리고 parent 는 그 노드의 부모 노드를 가리키도록 찾아냅니다.
                while successor.left:
                    parent = successor
                    successor = successor.left
                
                # 삭제하려는 노드인 node 에 successor 의 key 와 data 를 대입합니다.
                node.key = successor.key
                node.data = successor.data

                # 이제, successor 가 parent 의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                # 그에 따라 parent.left 또는 parent.right 를
                # successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 합니다.
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
                    

            return True

        else:
            return False



tree = BinSearchTree()
print(tree.insert(5, "1"))
print(tree)
