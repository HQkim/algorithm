# BOJ 1107.py


def solution():
    N = int(input())
    if N == 100:        # N이 100이면 0 리턴
        print(0)
        return

    M = int(input())
    if M:
        brokens = input().rstrip().split()
    else:
        brokens = []
        
    possibles = []
    for i in range(10):
        if str(i) not in brokens:
            possibles.append(str(i))

    min_cnt = int(10e9)
    is_plus = '+' not in brokens
    is_minus = '-' not in brokens

    if (N > 100 and is_plus) or (N < 100 and is_minus): # +, -로 이동이 가능할 경우
        min_cnt = abs(N - 100)


    def back(num, deci):    # 백트래킹으로 체크
        nonlocal N, min_cnt, is_minus, is_plus
        if len(str(N))-1 <= deci <= len(str(N))+1:  # N의 자리수 +- 1일때 체크하기
            if N == int(num):
                min_cnt = min(min_cnt, deci)
            elif (N > int(num) and is_plus) or (N < int(num) and is_minus):
                min_cnt = min(min_cnt, deci + abs(N-int(num)))
        
        if deci > len(str(N)) + 1:
            return
        
        if num == '0':
            return

        for i in possibles:
            if i == 0 and deci == 1:
                continue
            back(num+i, deci + 1)


    for i in possibles:
        back(i, 1)

    print(min_cnt)


solution()


# 백트래킹으로 문제를 풀었는데 아래에 그냥 set로 체크해서 푸는 풀이가 있다..
# +, - 버튼은 고장나지 않는다는 것을 전제로 하는 풀이다
# N = int(input())
# M = int(input())
# if M:
#     brokens = set(map(int, input().split()))
# else:
#     brokens = set()

# cnt_min = abs(N-100)
# for i in range(1000001):
#     flag = 0
#     for j in str(i):
#         if int(j) in brokens:
#             flag = 1
#             break
#     if not flag:
#         cnt_min = min(cnt_min, abs(N-i)+len(str(i)))
# print(cnt_min)