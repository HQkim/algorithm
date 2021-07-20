import sys

while True:
    num_list = list(map(int, sys.stdin.readline().rstrip().split()))

    if num_list[0] == 0:
        break

    num_list.sort()

    left = num_list[0]**2 + num_list[1]**2
    right = num_list[2]**2

    if left == right:
        print("right")
    else:
        print("wrong")
