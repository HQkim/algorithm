def solution(enroll, referral, seller, amount):
    l = len(enroll)
    answer = [0] * l

    # referral & seller index로 변환
    ref = []
    for i in referral:
        if i != "-":
            ref.append(enroll.index(i))
        else:
            ref.append(-1)
    print(ref)

    sell = []
    for i in seller:
        sell.append(enroll.index(i))
    print(sell)

    # 종속 그래프 만들기
    graph = [[] for _ in range(l)]

    for i in range(l):
        start = i
        while True:
            r = ref[start]
            if r == -1:  # 종속되는 것이 없음.
                break
            graph[i].append(r)
            start = r
    print(graph)

    # 이익 배분 현황
    for i in range(len(sell)):
        s = sell[i]
        if not graph[s]:
            give = int(0.1 * amount[i] * 100)
            profit = amount[i] * 100 - give
            answer[s] += profit
        else:
            give = int(0.1 * amount[i] * 100)
            profit = amount[i] * 100 - give
            answer[s] += profit
            for j in range(len(graph[s])):
                a = graph[s][j]

                give_pre = int(0.1*give)
                profit = give - give_pre
                give = give_pre
                answer[a] += profit

    print(answer)

    return answer


solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward",
                                                                                "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10])
