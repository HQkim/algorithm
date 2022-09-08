# programmers 2021카카오인턴십 표 편집

def solution(n, k, cmd):
    arr = [1] * n
    stack = []
    now = k
    last = n-1
    
    def move(a, c):
        nonlocal now
        
        if a == 'D':
            plus = 1
        else:
            plus = -1
            
        while c:
            now += plus
            if arr[now]:
                c -= 1
    
    
    def find_last(now):
        for i in range(now-1, -1, -1):
            if arr[i] == 1:
                return i
            

    def find_next(x):
        for i in range(x+1, n):
            if arr[i] == 1:
                return i
            
            
    for c in cmd:
        if c == 'C':
            arr[now] = 0
            stack.append(now)
            if now == last:
                now = find_last(now)
                last = now
            else:
                now = find_next(now)
            
        elif c == 'Z':
            rec = stack.pop()
            arr[rec] = 1
            if rec > last:
                last = rec
        else:
            action, cnt = c.split()
            cnt = int(cnt)
            move(action, cnt)        
    
    for i in range(n):
        arr[i] = 'O' if arr[i] else 'X'
    
    return ''.join(arr)


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))