# programmers 2020카카오 기둥과 보 설치

def solution(n, build_frame):
    answer = set()

    for x, y, a, b in build_frame:
        if b == 1:
            if a == 0 and check_pillar(x, y, answer, n):        # 기둥 설치 체크
                answer.add((x, y, a))
            elif a == 1 and check_beam(x, y, answer, n):        # 보 설치 체크
                answer.add((x, y, a))
        else:
            if a == 0:                                          # 기둥 삭제 체크
                answer.remove((x, y, a))
                if (x, y+1, 0) in answer and not check_pillar(x, y+1, answer, n):
                    answer.add((x, y, a))
                    continue
                if (x, y+1, 1) in answer and not check_beam(x, y+1, answer, n):
                    answer.add((x, y, a))
                    continue
                if (x-1, y+1, 1) in answer and not check_beam(x-1, y+1, answer, n):
                    answer.add((x, y, a))
                    continue
            else:                                               # 보 삭제 체크
                answer.remove((x, y, a))    
                if (x, y, 0) in answer and not check_pillar(x, y, answer, n):
                    answer.add((x, y, a))
                    continue
                if (x+1, y, 0) in answer and not check_pillar(x+1, y, answer, n):
                    answer.add((x, y, a))
                    continue
                if (x-1, y, 1) in answer and not check_beam(x-1, y, answer, n):
                    answer.add((x, y, a))
                    continue
                if (x+1, y, 1) in answer and not check_beam(x+1, y, answer, n):
                    answer.add((x, y, a))
                    continue

    answer = list(answer)
    answer = [[arr[0], arr[1], arr[2]] for arr in answer]
    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer


# 기둥이 설치될(or 유지될) 수 있는지 체크하는 함수
def check_pillar(x, y, arr, n):
    if y == 0:
        return True

    for nx, ny, a in arr:
        if nx == x and ny == y - 1 and a == 0:
            return True
        if nx == x and ny == y and a == 1:
            return True
        if nx == x - 1 and ny == y and a == 1:
            return True

    return False


# 보가 설치될(or 유지될) 수 있는지 체크하는 함수
def check_beam(x, y, arr, n):
    is_beam_a = 0
    is_beam_b = 0
    for nx, ny, a in arr:
        if a == 0 and ((nx == x and ny == y - 1) or (nx == x + 1 and ny == y - 1)):
            return True
        if a == 1 and nx == x - 1 and ny == y:
            is_beam_a = 1
        if a == 1 and nx == x + 1 and ny == y:
            is_beam_b = 1

    if is_beam_a and is_beam_b:
        return True

    return False

# print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(6, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))