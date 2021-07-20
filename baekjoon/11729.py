def hanoi(n, from_pos, to_pos, aux_pos, count, memo):
    if n ==1:        
        memo.append((from_pos, to_pos))
        count.append(1)
        return

    hanoi(n-1, from_pos, aux_pos, to_pos, count, memo)

    memo.append((from_pos, to_pos))
    count.append(1)

    hanoi(n-1, aux_pos, to_pos, from_pos, count, memo)

n = int(input())

count = []
memo = []

hanoi(n, 1, 3, 2, count, memo)

print(len(count))

for i in memo:
    print(i[0], i[1])