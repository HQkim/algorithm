# problem 9663
# 백트래킹 - N Queen

import sys
import time
# sys.setrecursionlimit(99999)


def bt(N, queen):
    global count
    if len(queen) == N:
        count += 1
        return

    for i in range(N):
        if not queen:
            queen.append(i)
            bt(N, queen)
            queen.pop()
        else:
            possible = True
            for index, p in enumerate(queen):
                if i == p or i == p+len(queen)-index or i == p-(len(queen)-index):
                    possible = False
                    break
            if possible:
                queen.append(i)
                
                bt(N, queen)
                queen.pop()


N = int(sys.stdin.readline().rstrip())

start = time.time()

count = 0
bt(N, [])

print(count)
print(time.time()-start)


# 소감
# 위의 코드는 질문란에서 다른 사람이 짜놓은 코드를 복사해 온 것이다.
# 읽었을 때는 대충 이해되는 듯했지만
# 내가 이틀에 걸쳐 머리를 굴려도 잘 짜지 못했다.
# 재귀함수 쓰는건 넘나 어렵다.
# 내가 스스로 코드를 짠 것이 있는데 지저분해서 다 지워버렸다.
# 거기서 문제가 생겼던 것은 a_list 를 global로 지정하고 함수 내부에서 돌아가게 했는데
# n = 3 일 때 [x, y, z] 이런 식으로 나와야 하는데 [z, z, z]와 같이 마지막 값으로 다 중복되어 결과가 나왔다.
# 이해가 잘 안갔다.
