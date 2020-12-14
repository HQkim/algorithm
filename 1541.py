# 잃어버린 괄호

import sys

exp = sys.stdin.readline().rstrip()  # exp == 수식
exp.replace(")", "")
exp.replace("(", "")
exp_minus_split = exp.split("-")
exp_minus_split_abs_sum = []

for i in range(len(exp_minus_split)):
    exp_minus_split_plus_split = exp_minus_split[i].split("+")
    plus_sum = 0
    for j in range(len(exp_minus_split_plus_split)):
        plus_sum += int(exp_minus_split_plus_split[j])
    exp_minus_split_abs_sum.append(plus_sum)

result = 0
for i in range(len(exp_minus_split_abs_sum)):
    if i == 0:
        result += exp_minus_split_abs_sum[i]
    else:
        result -= exp_minus_split_abs_sum[i]

print(result)


# 그리디 알고리즘
# Silver2, 정답렬 48.373%
# 소감: 괄호를 하나만 쳐야 하는 줄 알았다. 그래서 exp_minus_split_abs_sum이 가장 큰 녀석을 찾고
#      거기서 또 sum이 같으면 - 바로 뒤의 절대값이 큰 숫자를 고르려고 했다 보니 코드가 길어졌다.
#      결국엔 문제를 잘 읽어야 하는 ㅎㅎ..
