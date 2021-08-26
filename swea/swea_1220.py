# swea 1220 Magnetic
'''
N극
arr
S극

7
1 0 2 0 1 0 1
0 2 0 0 0 0 0
0 0 1 0 0 1 0
0 0 0 0 1 2 2 
0 0 0 0 0 1 0
0 0 2 1 0 2 1
0 0 1 2 2 0 2

'''
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]   # 1은 아래로, 2는 위로

    count = 0
    for j in range(N):
        flag = False
        for i in range(N):
            if arr[i][j] == 1:
                flag = True
            elif arr[i][j] == 2:
                if flag:
                    count += 1
                    flag = False 
    
    print(f'#{tc} {count}')