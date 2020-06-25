# 이진트리의 구현 - 노드(node)
class Node:
    # 생성자
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
        
    # 노드의 갯수 구하는 함수 - 재귀함수 이용
    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1
    
    # depth
    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return max(l,r) + 1
    
    # 중위 순회
    def inorder(self):
        traversal = []
        
        # 왼쪽 서브트리가 존재한다면
        if self.left:
            traversal += self.left.inorder()
        
        traversal.append(self.data)
        
        # 오른쪽 서브트리가 있다면
        if self.right:
            traversal += self.right.inorder()
            
        return traversal

    # 전위 순회
    def preorder(self):
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal
    
    # 후위 순회
    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        
        if self.right:
            traversal += self.right.postorder()
            
        traversal.append(self.data)
        return traversal
        

# 이진 트리의 구현 - 트리(tree)
class BinaryTree:
    # 생성자
    def __init__(self, r):
        self.root = r
        
    # 크기 구하기
    def size(self):
        # 루트가 존재하면 리턴
        if self.root:
            return self.root.size()
        else:
            return 0
        
    # depth
    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0
            
        
    # 중위 순회
    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    # 전위 순회
    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []
            
    # 후위순회
    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []