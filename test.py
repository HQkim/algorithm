arry = [[100, 100, 90], [90, 90, 80], [90, 95, 90]]


def solution(arry):
    answer = []

    number_of_students = len(arry)
    for i in range(number_of_students):
        scores = [x[i] for x in arry]
        score_max = max(scores)
        score_min = min(scores)

        if scores[i] == score_max and scores.count(score_max) == 1:
            score = (sum(scores) - score_max) / (number_of_students - 1)
            answer.append(score)
            continue
        if scores[i] == score_min and scores.count(score_min) == 1:
            score = (sum(scores) - score_min) / (number_of_students - 1)
            answer.append(score)
            continue
        score = sum(scores) / number_of_students
        answer.append(score)
    print(answer)


solution(arry)
