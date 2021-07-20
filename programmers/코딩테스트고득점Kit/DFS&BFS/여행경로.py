def solution(tickets):
    answer = []

    # 그래프 만들기
    d = {}
    for t in tickets:
        if d.get(t[0]):
            d[t[0]].append(t[1])
        else:
            d[t[0]] = [t[1]]
    
    graph = []
    for k,v in d.items():
        graph.append([k,v])

    for i in range(len(graph)):
        graph[i][1].sort()
        if graph[i][0] == "ICN":
            start = i


    print(graph, start)
    
    return answer

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
