# BOJ 10799 쇠막대기

rods = input().rstrip()

n = len(rods)

result = 0
rod_cnt = 0
for i in range(n):
    if rods[i] == '(':
        if rods[i+1] == ')':
            result += rod_cnt
        else:
            rod_cnt += 1
    else:
        if rods[i-1] == '(':
            continue
        else:
            rod_cnt -= 1
            result += 1

print(result)