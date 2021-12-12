# programmers_2019카카오 오픈채팅방

def solution(record):
    answer = []
    result = []
    names = {}

    for r in record:
        r_split = r.split()
        action = r_split[0]
        user_id = r_split[1]

        if action in ["Enter", "Change"]:
            nickname = r_split[2]
            names[user_id] = nickname
            if action == "Enter":
                result.append((action, user_id))
        else:
            result.append((action, user_id))

    for res in result:
        if res[0] == "Enter":
            answer.append(f"{names[res[1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{names[res[1]]}님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
