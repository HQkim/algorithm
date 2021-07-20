import sys

n, m = map(int, sys.stdin.readline().split())
pos = list(map(int, sys.stdin.readline().split()))

map_origin = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# 왼쪽으로 방향 트는 함수


def turn(x):
    d = x[2]
    if d == 0:
        d = 3
    else:
        d -= 1
    x[2] = d
    return x


# 보는 방향으로 이동했을 때의 임시 위치
def temporary_pos(x):
    d = x[2]
    if d == 0:
        x[0] -= 1
    elif d == 1:
        x[1] += 1
    elif d == 2:
        x[0] += 1
    else:
        x[1] -= 1
    return x


# 체크하고 움직이는 함수
def move(pos, count):
    # 시작 위치 1로 만들기
    if count == 0:
        map_origin[pos[0]][pos[1]] = 1

    # 왼쪽으로 방향틀기
    pos = turn(pos)
    print(pos, '함수 들어와서')

    # 임시 position 정의
    tem_pos = [0]*3
    for i in range(len(pos)):
        tem_pos[i] = pos[i]
    tem_pos = temporary_pos(tem_pos)
    print(pos, 'tem_pos 하고')

    # 보는 방향이 가본적 있는지 체크하기
    map_check = map_origin[tem_pos[0]][tem_pos[1]]

    # 4방향 모두 갈 수 없는 경우 체크하기
    all_check = map_origin[pos[0]-1][pos[1]]*map_origin[pos[0]+1][pos[1]
                                                                  ]*map_origin[pos[0]][pos[1]-1]*map_origin[pos[0]][pos[1]+1]

    if all_check == 1:          # 4방향 모두 갈 수 없는 경우 종료
        print(pos, 'finish')
        print(map_origin)
        return count
    elif map_check == 1:        # 이쪽 방향 못가는 경우 다시 함수호출(재귀)
        print(pos, '여기로 못감')
        print(map_origin)
        return move(pos, count)
    else:                       # 갈 수 있는 경우 진행
        pos = tem_pos
        map_origin[tem_pos[0]][tem_pos[1]] = 1
        count += 1
        print(pos, '이동')
        print(map_origin)
        return move(pos, count)


print(pos)

count = 0

result = move(pos, count)
print(result+1)
