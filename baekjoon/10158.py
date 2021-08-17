# 백준 10158 개미

import sys

input = sys.stdin.readline


def solution(w, h, p, q, t):

    w_list = []
    h_list = []

    for i in range(w):
        w_list.append(i)
    for i in range(w, 0, -1):
        w_list.append(i)

    for i in range(h):
        h_list.append(i)
    for i in range(h, 0, -1):
        h_list.append(i)

    x_t = w_list[(p+t) % (2*w)]
    y_t = h_list[(q+t) % (2*h)]

    return x_t, y_t


if __name__ == "__main__":
    w, h = map(int, input().split())
    p, q = map(int, input().split())
    t = int(input())

    x, y = solution(w, h, p, q, t)
    print(x, y)

# https://hyunsix.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-10158-%EA%B0%9C%EB%AF%B8?category=891807 참고
