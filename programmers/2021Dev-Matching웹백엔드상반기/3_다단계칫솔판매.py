# programmers 2021 Dev-Matching: 웹 백엔드 개발(상반기) 다단계 칫솔 판매
def solution(enroll, referral, seller, amount):
    answer = []
    parents = {}
    shares = {}

    for i in range(len(enroll)):
        parents[enroll[i]] = referral[i]
        shares[enroll[i]] = 0
    
    for i in range(len(seller)):
        now = seller[i]
        money = amount[i] * 100
        while 1:
            to_share = money // 10
            my_share = money - to_share
            shares[now] += my_share
            now = parents[now]
            money = to_share
            if money == 0 or now == '-':
                break
    
    for e in enroll:
        answer.append(shares[e])

    return answer


solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward",
                                                                                "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10])
