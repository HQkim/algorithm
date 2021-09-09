def solution(numbers):
    visited = [1]*10
    answer = sum(range(10))
    for n in numbers:
        if visited[n]:
            answer -= n
            visited[n] = 0

    return answer


print(solution([5, 8, 4, 0, 6, 7, 9]))
