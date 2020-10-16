n, m = map(int, input().split())

wood = list(map(int, input().split()))

start = 0
end = max(wood)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in wood:
        if x > mid:
            total += (x - mid)

    if total < m:
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)
