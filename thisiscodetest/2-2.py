# 큰 수의 법칙
# 5 8 3 (n, m, k)
# 2 4 5 4 6 (배열)
# 위와 같이 입력값이 주어졌을 때 배열의 수를 m번 더하는데 이 때 연속으로 k번 초과하여 더해질
# 수는 없는 경우에 가장 최대가 되는 결과값을 출력하여라. 위의 경우 답은 6+6+6+5+6+6+6+5인 46이다.
import time

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

t = time.time()
a.sort()
first = a[n-1]
second = a[n-2]
T = 0

if first == second:
    T = first * m
else:
    while(True):
        T += first*k
        m -= k
        if m > k:
            T += second
            m -= 1
        elif m > 0 and m <= k:
            T += second
            m -= 1
            if m == 0:
                break
            else:
                T += first*m
                break
        else:
            m += k
            T += (second+first(m-1))
            break
print(T)

print(time.time()-t)
