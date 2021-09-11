import copy


def solution(n, info):
    answer = []
    max_diff = 0

    # 완전탐색 (10-step: 현재 검사하는 점수, left: 남은 발 수, arr: 현재까지 화살을 기록한 배열)
    def back(step, left, arr):
        nonlocal max_diff, answer
        if step == 10:                              # 0점까지 도착했을 때
            arr.append(left)
            total = 0
            for i in range(11):
                if arr[i] > info[i]:
                    total += 10-i
                elif arr[i] == 0 == info[i] == 0:
                    pass
                else:
                    total -= 10-i

            if total >= max_diff:                   # 최고점을 갱신한다면
                max_diff = total
                answer = copy.deepcopy(arr)
            arr.pop()
            return

        info_step = info[step]
        if left > info_step:                        # 라이언이 현재 점수에서 이기는 경우
            arr.append(info_step+1)
            back(step+1, left-info_step-1, arr)
            arr.pop()

        arr.append(0)                               # 라이언이 현재 점수를 안맞추는 경우
        back(step+1, left, arr)
        arr.pop()

    back(0, n, [])

    if max_diff == 0:
        return [-1]

    return answer


solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
