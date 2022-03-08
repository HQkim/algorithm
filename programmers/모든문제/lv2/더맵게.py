# programmers lv2 더 맵게
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)         # 리스트를 즉각적으로 heap으로 변환함 O(N)
    while scoville:
        least_hot = heapq.heappop(scoville)
        if least_hot >= K:
            break
        if not scoville:
            return -1
        second_least_hot = heapq.heappop(scoville)
        mix_hot = least_hot + second_least_hot * 2
        heapq.heappush(scoville, mix_hot)
        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))