def solution(n, k, cmd):
    answer = ''

    a = ["O"]*n
    stack = []
    d = 0
    last = n-1
    for c in cmd:
        if c == "C":  # 삭제
            a[k] = "X"
            stack.append(k)
            if k == last:
                while True:
                    k -= 1
                    print("삭제", k)
                    if a[k] == "O":
                        last = k
                        break
            else:
                while True:
                    print("삭제", k)
                    k += 1
                    if a[k] == "O":
                        break
            continue
        if c == "Z":  # 복구
            d = stack.pop()
            a[d] = "O"
            if d > last:
                last = d
            continue
        if c[0] == "U":  # 위로
            move = int(c[2:])
            while move != 0:
                k -= 1
                if a[k] == "O":
                    move -= 1
            continue
        if c[0] == "D":  # 아래로
            move = int(c[2:])
            while move != 0:
                k += 1
                if a[k] == "O":
                    move -= 1

    answer = "".join(a)
    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
