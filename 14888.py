import sys
from itertools import permutations

# INPUT 및 상수 설정
input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().rstrip().split()))
number_operator = list(map(int, input().rstrip().split()))
INF = int(1e9)

# 연산자 모든 조합
arry_operator = []
for i in range(len(number_operator)):
    arry_operator += [i] *number_operator[i]

permu_operator = list(set(permutations(arry_operator, n-1)))

# 최대 최소 찾기
mini = INF
maxi = -INF
for op in permu_operator:
    result = a_list[0]
    for i in range(n-1):
        o_i = op[i]
        if o_i == 0:
            result += a_list[i+1]
        elif o_i == 1:
            result -= a_list[i+1]
        elif o_i ==2:
            result *= a_list[i+1]
        else:
            if result < 0:                
                result = -(abs(result) // a_list[i+1])
            else:
                result = result // a_list[i+1]

    if result > maxi:
        maxi = result
    if result < mini:
        mini = result

print(maxi)
print(mini)
    
