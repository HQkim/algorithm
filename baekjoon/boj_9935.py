# BOJ 9935 문자열 폭발
import sys


def process(word, bomb):
    stack = []
    m = len(bomb)
    bomb_last = bomb[-1]

    for w in word:
        stack.append(w)
        if w == bomb_last and len(stack) >= m and ''.join(stack[len(stack)-m:]) == bomb:
            for _ in range(m):
                stack.pop()

    if stack:
        return ''.join(stack)
    else:
        return 'FRULA'


if __name__ == '__main__':
    input = sys.stdin.readline
    word = input().rstrip()
    bomb = input().rstrip()
    result = process(word, bomb)
    print(result)