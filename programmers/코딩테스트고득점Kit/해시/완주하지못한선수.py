def solution(participant, completion):
    
    dic_par = {string:0 for string in participant}
    dic_com = {string:0 for string in completion}
    
    for par in participant:
        dic_par[par] += 1     
    
    for com in completion:
        dic_com[com] += 1

    answer=''
    for k,v in dic_par.items():
        if k in dic_com and v != dic_com[k]:
            answer = k
            break
        elif k not in dic_com:
            answer = k
            break
            
    return answer