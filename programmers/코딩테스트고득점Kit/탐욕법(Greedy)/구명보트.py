from collections import deque

# 상우로부터 해법을 듣고 구현 (아 이건 2명 이상 사람이 들어갈 수 있음)
def solution(people, limit):

    people_sorted = deque(sorted(people))
    number_boat = 0
    boat = []
    while True:
        print("시작",people_sorted, boat, number_boat)

        # break
        if not people_sorted and not boat:
            break
        
        # boat 채우기
        if not boat:
            boat.append(people_sorted[-1])
            people_sorted.pop()
        else:
            if people_sorted:
                boat.append(people_sorted[0])
                weight = sum(boat)
                if weight < limit:
                    people_sorted.popleft()
                elif weight == limit:
                    people_sorted.popleft()
                    boat.clear()
                    number_boat += 1
                else:
                    boat.clear()
                    number_boat += 1
            else:
                boat.clear()
                number_boat += 1
        print("끝",people_sorted, boat, number_boat)

        
    return number_boat

print(solution([70, 80, 50], 100))

# 같은 원리인데 훨씬 간단한 코드 (아 문제에서 2명이 최대 탈 수 있다고 함)
def solution2(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
        return len(people) - answer

print(solution2([10, 10, 80], 100))