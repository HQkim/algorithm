# 9184번


# 이 코드는 다른 사람의 코드를 참고했는데 10배 이상 빠르다.
import sys
input = sys.stdin.readline

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
# 재귀로 준 변수를 각각의 함수 칸으로 만든다고 생각
def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20,20,20)
    if dp[a][b][c] != 0:
        return dp[a][b][c]
    
    if a < b and b < c:
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
        return dp[a][b][c]

while True:
    a,b,c = map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print("w(%d, %d, %d) = %d"%(a,b,c,w(a,b,c)))





# 이 풀이는 전체 값을 모두 계산해서 느리다.
'''
def w_func(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a < b and b < c: 
        return w_func(a, b, c-1) + w_func(a, b-1, c-1) - w_func(a, b-1, c)
    return w_func(a-1, b, c) + w_func(a-1, b-1, c) + w_func(a-1, b, c-1) - w_func(a-1, b-1, c-1)

w = dict()

for a in range(-50,51):
    for b in range(-50, 51):
        for c in range(-50, 51):
            if a <= 0 or b <= 0 or c <= 0:
                w[(a,b,c)] = 1

for a in range(1, 21):
    for b in range(1, 21):
        for c in range(1, 21):
            if a < b and b < c:
                if not w.get((a,b,c-1)):
                    x = w_func(a,b,c-1)
                else:
                    x = w[(a,b,c-1)]
                if not w.get((a,b-1,c-1)):
                    y = w_func(a,b-1,c-1)
                else:
                    y = w[(a, b-1, c-1)]
                if not w.get((a,b-1,c)):
                    z = w_func(a,b-1,c)
                else:
                    z = w[(a,b-1,c)]
                w[(a,b,c)] = x + y - z
            else:
                if not w.get((a-1,b,c)):
                    i = w_func(a-1,b,c)
                else:
                    i = w[(a-1,b,c)]
                if not w.get((a-1,b-1,c)):
                    j = w_func(a-1,b-1,c)
                else:
                    j = w[(a-1,b-1,c)]
                if not w.get((a-1,b,c-1)):
                    k = w_func(a-1,b,c-1)
                else:
                    k = w[(a-1,b,c-1)]
                if not w.get((a-1,b-1,c-1)):
                    l = w_func(a-1,b-1,c-1)
                else:
                    l = w[(a-1,b-1,c-1)]
                w[(a,b,c)] = i + j + k - l 

w_20 = w[(20,20,20)]

for a in range(1, 51):
    for b in range(1, 51):
        for c in range(1, 51):
            if a > 20 or b > 20 or c > 20:
                w[(a,b,c)] = w_20



while True:
    a,b,c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break

    print("w({}, {}, {}) =".format(a,b,c),w[(a,b,c)])
'''   
        