def solution(n, left, right):
    left_row = (left+1) // n
    right_row = (right+1) // n
    left_res = (left+1) % n
    right_res = (right+1) % n

    if left_res:
        left_row += 1
    if right_res:
        right_row += 1

    arr = []
    for i in range(left_row-1, right_row):
        sub_arr = [0] * n
        for j in range(n):
            if j >= i:
                sub_arr[j] = j+1
            else:
                sub_arr[j] = i+1
        arr += sub_arr

    answer = arr[left % n:left % n+(right-left)+1]

    return answer


print(solution(3, 2, 5))
print(solution(4, 7, 14))
