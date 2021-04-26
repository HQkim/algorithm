import sys
input = sys.stdin.readline

class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

def preorder(node): # 전위 순회
    print(node.item, end ="")
    if node.left != ".":
        preorder(tree[node.left])
    if node.right != ".":
        preorder(tree[node.right])

def inorder(node): # 중위 순회
    if node.left !=".":
        inorder(tree[node.left])
    print(node.item, end="")
    if node.right != ".":
        inorder(tree[node.right])

def postorder(node): # 후위 순회
    if node.left != ".":
        postorder(tree[node.left])
    if node.right != ".":
        postorder(tree[node.right])
    print(node.item, end="")


if __name__ == "__main__":

    N = int(input())
    tree = {}

    for _ in range(N):
        node, left, right = map(str, input().rstrip().split())
        tree[node] = Node(item=node, left=left, right=right)

    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree["A"])


# 어렵다 클래스로 트리 구현도 그리고 순회도. 하다 보면 익숙해 지겠지...