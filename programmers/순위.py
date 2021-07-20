def solution(n, results):
    my_losers, my_winers = {}, {}

    for i in range(1, n+1):
        my_losers[i] = set()
        my_winers[i] = set()

    for i in range(1, n+1):
        for result in results:
            if result[0] == i:
                my_losers[i].add(result[1])
            if result[1] == i:
                my_winers[i].add(result[0])

        for loser in my_losers[i]:
            my_winers[loser].update(my_winers[i])

        for winner in my_winers[i]:
            my_losers[winner].update(my_losers[i])

    count = 0
    for i in range(1, n+1):
        if len(my_winers[i]) + len(my_losers[i]) == n-1:
            count += 1

    return count


solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
