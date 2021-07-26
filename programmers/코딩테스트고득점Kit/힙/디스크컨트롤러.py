# 프로그래머스 디스크 컨트롤러

def solution(clothes):
    cloth_dict = {}

    for c in clothes:
        cloth_type = c[1]
        cloth = c[0]
        if cloth_type not in cloth_dict:
            cloth_dict[cloth_type] = [cloth]
        else:
            cloth_dict[cloth_type] += [cloth]

    result = 1
    for v in cloth_dict.values():
        result *= len(v) + 1

    return result - 1


print(solution([["yellowhat", "headgear"], [
      "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
