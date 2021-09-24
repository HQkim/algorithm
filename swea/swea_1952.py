# swea 1952 수영장

def f(m, pay):
    global min_pay
    if m > 12:                      # 최종 이용료가 최소값인지 확인
        min_pay = min(pay, min_pay)
        return

    if plan[m] == 0:                # 이용횟수가 0인 달은 패스
        f(m+1, pay)
    else:
        f(m+1, pay+day*plan[m])     # 1일 이용권으로 이용
        f(m+1, pay+month)           # 1달 이용권으로 이용
        f(m+3, pay+three_month)     # 3달 이용권으로 이용


T = int(input())
for tc in range(1, T+1):
    day, month, three_month, year = map(int, input().split())
    plan = [0]+list(map(int, input().split()))
    min_pay = year

    f(1, 0)

    print(f'#{tc} {min_pay}')
