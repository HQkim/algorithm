# programmers 2019카카오인텁십 불량사용자

def solution(user_id, banned_id):
    answer = 0
    answer_set = set()

    # 불량 사용자 아이디의 후보를 구하기
    banned_id_list = [[] for _ in range(len(banned_id))]

    for k in range(len(banned_id)):             # banned_id를 순회
        b_id = banned_id[k]
        for j in range(len(user_id)):           # user_id를 순회
            u_id = user_id[j]
            if len(b_id) != len(u_id):          # 길이가 다르면 패스
                continue
            is_p = True
            for i in range(len(b_id)):
                if b_id[i] != '*' and u_id[i] != b_id[i]:
                    is_p = False
            if is_p:
                banned_id_list[k].append(j)
    
    # 불량 사용자 아이디의 후보를 이용해서 가능한 경우의 수 구하기
    n = len(user_id)
    m = len(banned_id)
    visited = [0] * n
    def dfs(d):

        if d == m:
            answer_set.add(''.join(map(str, visited)))
            return

        for i in banned_id_list[d]:
            if not visited[i]:
                visited[i] = 1
                dfs(d+1)
                visited[i] = 0

    dfs(0)
    answer = len(answer_set)

    return answer

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])