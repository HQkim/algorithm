# BOJ 9012 괄호

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    word = input().strip()
    count = 0
    for w in word:
        if w == '(':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            break
    
    answer = 'YES' if count ==0 else "NO"
    print(answer)