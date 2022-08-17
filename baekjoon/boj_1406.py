# BOJ 1406 에디터

import sys
from collections import deque

input = sys.stdin.readline

left = deque(list(input().rstrip()))    # 커서 왼쪽의 문자들
right = deque()                         # 커서 오른쪽의 문자들
m = int(input().rstrip())

for _ in range(m):
    cmd_line = input().rstrip().split()
    if len(cmd_line) == 2:  # 문자 삽입
        word = cmd_line[1]
        left.append(word)
    else:
        cmd = cmd_line[0]
        if cmd == 'L' and left:             # 커서 왼쪽으로 이동
            right.appendleft(left.pop())
        elif cmd == 'D' and right:          # 커서 오른쪽으로 이동
            left.append(right.popleft())
        elif cmd == 'B' and left:           # 커서 왼쪽 문자 삭제
            left.pop()
print(''.join(left)+''.join(right))
        
            


