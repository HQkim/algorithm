# programmers 2019_카카오블라인드

from itertools import combinations


def solution(relation):
    answer = 0

    candidate_keys = []
    N = len(relation[0])
    indexes = list(range(N))

    for i in range(1, N+1):
        combs = combinations(indexes, i)
        for comb in combs:
            is_minimality = check_minimality(comb, candidate_keys)
            
            if not is_minimality:
                continue
            
            is_uniqueness = check_uniqueness(comb, relation)

            if is_uniqueness:
                candidate_keys.append(comb)
    
    answer = len(candidate_keys)
    print(candidate_keys)
    
    return answer


def check_minimality(comb, candidate_keys):
    
    is_minimality = True
    for key in candidate_keys:
        
        is_minimality = True
        for k in key:
            if k not in comb:
                break
        else:
            is_minimality = False
        
        if not is_minimality:
            break
    
    return is_minimality


def check_uniqueness(comb, relation):
    check_set = set()

    is_uniqueness = True
    for rel in relation:
        element = tuple([rel[i] for i in comb])
        if element not in check_set:
            check_set.add(element)
        else:
            is_uniqueness = False
            break
    
    return is_uniqueness
        


solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],
["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])