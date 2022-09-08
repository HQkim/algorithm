# programmers 2022카카오인턴십 성격유형검사하기

def solution(survey, choices):
    answer = ''

    d = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    n = len(survey)

    for i in range(n):
        choice = choices[i]
        if choice > 4:
            d[survey[i][1]] += choice - 4
        elif choice < 4:
            d[survey[i][0]] += 4 - choice

    word_RT = 'R' if d['R'] >= d['T'] else 'T'
    word_CF = 'C' if d['C'] >= d['F'] else 'F'
    word_JM = 'J' if d['J'] >= d['M'] else 'M'
    word_AN = 'A' if d['A'] >= d['N'] else 'N'

    answer = word_RT + word_CF + word_JM + word_AN

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))