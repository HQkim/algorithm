from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    answer = 0
    d = deque()

    for city in cities:
        city = city.lower()

        if city in d:   # hit
            d.remove(city)
            d.appendleft(city)
            answer += 1
        else:           # miss
            if len(d) < cacheSize:
                d.appendleft(city)
            else:
                d.pop()
                d.appendleft(city)
            answer += 5
                
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))