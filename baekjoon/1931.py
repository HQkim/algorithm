# 회의실배정
# 1931번


n = int(input())

information = [tuple(map(int, input().split())) for _ in range(n)]
information = sorted(information, key=lambda x: (x[1], x[0]))

count = 0
finish = 0
for i in range(n):
    if information[i][0] >= finish:
        count += 1
        finish = information[i][1]
print(count)


# 소감
# 끝나는 시간을 기준으로 정렬한 후 그리디 알고리즘을 적용해야 한다는 것은 발견했으나
# 계속 "틀렸습니다" 가 나와서 뭐가 문제인지 몰라서 검색을 해보니
# 2
# 2 2
# 1 2
# 같은 경우 처럼 시작 시간 정렬도 추가적으로 해줘야 하는 것을 알았다.

# 그리디 알고리즘
# 실버2 ,정답률 28.455%
