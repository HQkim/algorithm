# 크루스칼 알고리즘
def solution(n, costs):
    
    costs.sort(key= lambda x:x[2])
    
    mst = []
    p = [0] # 상호배타적 집합

    for i in range(1,n+1):
        p.append(i)

    def find(u):
        if u != p[u]:
            p[u] = find(p[u])
        return p[u]

    def union(u, v):
        root1 = find(u)
        root2 = find(v)
        p[root2] = root1 # 임의로 root2가 root1의 부모

    tree_edges = 0 # 간선 개수
    mst_cost = 0 # 가중치 합

    while True:
        if tree_edges == n-1:
            break
        print(costs, tree_edges, p)
        u, v, wt = costs.pop(0)
        if find(u) != find(v): # u와 v가 서로 다른 집합에 속해 있으면
            union(u,v)
            mst.append((u,v))
            mst_cost += wt
            tree_edges += 1

    print('최소진장트리: ', mst)
    print('최소신장트리 가중치: ', mst_cost)
    return mst

solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
