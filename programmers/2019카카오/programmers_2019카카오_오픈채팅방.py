# programmers_2019카카오 오픈채팅방

def solution(record):
    answer = [] # 정답 배열
    result = [] # uid 닉네임으로 바뀌기 전 배열

    name_dict = dict()  # uid-닉네임 딕셔너리

    # 결과 기록
    for cmd in record:
        cmd = cmd.split()
        if cmd[0] == 'Enter':
            result.append(cmd[:2])
            name_dict[cmd[1]] = cmd[2]
        elif cmd[0] == 'Leave':
            result.append(cmd[:2])
        else:
            name_dict[cmd[1]] = cmd[2]
    
    # uid 닉네임으로 바꾸기
    for cmd in result:
        name = f'{name_dict[cmd[1]]}님이 '
        if cmd[0] == 'Enter':
            action = '들어왔습니다.'
        else:
            action = '나갔습니다.'
        
        answer.append(name+action)

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
