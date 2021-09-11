def solution(id_list, report, k):
    answer = []

    # ID별 메일을 받은 횟수를 딕셔너리로 기록
    mail_count = {}
    for id in id_list:
        mail_count[id] = 0

    # 딕셔너리 = {신고당한ID : set(신고한 ID들),...}
    report_count = {}
    for r in report:
        id_report, id_reported = r.split()
        if report_count.get(id_reported):
            report_count[id_reported].add(id_report)
        else:
            report_count[id_reported] = {id_report}

    # 신고당한 횟수가 k를 넘으면 mail_count에서 갱신
    for value in report_count.values():
        if len(value) >= k:
            for id in value:
                mail_count[id] += 1

    # 유저별 메일을 받은 횟수 기록
    for id in id_list:
        answer.append(mail_count[id])

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo",
                                                    "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
