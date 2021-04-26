# 13305번

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
length_list = list(map(int, input().rstrip().split()))
price_list = list(map(int, input().rstrip().split()))

answer = 0
price_low = int(1e10)
for i in range(n-1):
    price = price_list[i]
    length = length_list[i]
    if price < price_low:
        price_low = price
    answer += price_low * length

# q_length = deque(length_list)
# q_price = deque(price_list)

# price_low = int(1e10)
# answer = 0
# while q_length:
#     price_pop = q_price.popleft()
#     length_pop = q_length.popleft()

#     if price_pop < price_low:
#         answer += price_pop*length_pop
#         price_low = price_pop
#     else:
#         answer += price_low*length_pop

print(answer)