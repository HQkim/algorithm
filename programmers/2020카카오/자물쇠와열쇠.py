# programmers 2020카카오 자물쇠와 열쇠

def solution(key, lock):
    answer = False
    N = len(lock[0])
    M = len(key[0])

    # 자물쇠의 홈을 기록
    up_cnt = 0
    for i in range(N):
        for j in range(N):
            if not lock[i][j]:
                up_cnt += 1

    # 회전한 배열들
    key_90 = rotate(key)
    key_180 = rotate(key_90)
    key_270 = rotate(key_180)
    
    # 열쇠로 자물쇠를 열 수 있는지 체크하는 함수(열수 있으면 True, 없으면 False) 
    def check(k, r, c):
        is_p = True
        dr = r - (M - 1)
        dc = c - (M - 1)

        cnt = 0 
        for i in range(M):
            for j in range(M):
                r_lock = i + dr
                c_lock = j + dc
                if 0 <= r_lock < N and 0 <= c_lock < N:
                    if not lock[r_lock][c_lock] and k[i][j]:  # 자물쇠 홈이고 열쇠는 돌기인 경우
                        cnt += 1
                    elif lock[r_lock][c_lock] and k[i][j]:  # 자물쇠와 열쇠 모두 돌기인 경우
                        is_p = False
                        break
            if not is_p:
                break

        if is_p and cnt == up_cnt:
            return True
        else:
            return False


    # 가능한 모든 경우에 대해 체크하기
    for i in range(N+M-1):
        for j in range(N+M-1):
            if check(key, i, j) or check(key_90, i, j) or check(key_180, i, j) or check(key_270, i, j):
                answer = True
                break
        if answer:
            break

    return answer


# 시계방향으로 90도 회전한 배열을 구하는 함수
def rotate(arr):
    m = len(arr[0])
    ret = [[0] * m for _ in range(m)]

    for r in range(m):
        for c in range(m):
            ret[c][m-1-r] = arr[r][c]

    return ret


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))