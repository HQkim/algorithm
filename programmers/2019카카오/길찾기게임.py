# programmers 2019카카오 길찾기게임
import sys

sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    # 노드 클래스
    class Node:
        def __init__(self, n, x, y):        # 번호, x좌표, y좌표로 초기화
            self.n = n
            self.x = x
            self.y = y
            self.left = self.right = None   # left와 right는 None으로 초기화


    # 이진트리 클래스
    class BinaryTree:                       
        def __init__(self):                 
            self.root = None
        
        def preorder(self):                 # 전위 순회
            def _preorder(node):
                pre.append(node.n)
                if node.left:
                    _preorder(node.left)
                if node.right:
                    _preorder(node.right)
            _preorder(self.root)

        def postorder(self):                # 후위 순회
            def _postorder(node):
                if node.left:
                    _postorder(node.left)
                if node.right:
                    _postorder(node.right)
                post.append(node.n)
            _postorder(self.root)
                

    N = len(nodeinfo)
    nodeinfo_num = [(i+1, nodeinfo[i][0], nodeinfo[i][1]) for i in range(N)]    # (노드번호, x좌표, y좌표)들의 리스트
    nodeinfo_num.sort(key=lambda x: -x[2])                                      # y값이 높은 순서대로 정렬 

    BT = BinaryTree()
    BT.root = Node(nodeinfo_num[0][0], nodeinfo_num[0][1], nodeinfo_num[0][2])

    for i in range(1, N):
        n, x, y = nodeinfo_num[i]
        stack = [BT.root]

        while stack:
            node = stack.pop()
            if x < node.x:                      # 왼쪽 서브트리인 경우
                if node.left:                       # left가 있으면 left 스택에 담기
                    node_left = node.left
                    stack.append(node_left)
                else:                               # left 없으면 left로 지정
                    node.left = Node(n, x, y)
            else:                               # 오른쪽 서브트리인 경우
                if node.right:                      # right가 있으면 right 스택에 담기
                    node_right = node.right
                    stack.append(node_right)
                else:                               # right 없으면 right로 지정
                    node.right = Node(n, x ,y)

    pre = []
    post = []
    BT.preorder()   # 전위순회
    BT.postorder()  # 후위순회

    answer = [pre, post]
    return answer


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))


# 이진트리의 전위순회, 후위순회에 대해서 구글링을 해가며 구현함