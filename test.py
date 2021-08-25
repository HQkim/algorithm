T = int(input())
for tc in range(1, T+1):
    x, y = map(int, input().split())

    m = min(x, y)                   # x,y 중 최소값
    m_10 = (m * 10**7)//2           # 2h = m이 되는 때까지
    max_v = 0
    for i in range(0, m_10):
        h = i / 10**7               # step을 1/10**7로
        v = h * (x-2*h) * (y-2*h)
        if v > max_v:
            max_v = v

    print(f'#{tc} {max_v:.6f}')

