# BOJ 6603 로또
import sys
from itertools import combinations

input = sys.stdin.readline
print = sys.stdout.write

if __name__ == "__main__":
    while 1:
        ins = input().rstrip()
        if ins == '0':
            break
        ins = list(map(int, ins.split()))
        k, numbers = ins[0], ins[1:]
        combis = list(map(lambda k: ' '.join(map(str, list(k))) ,combinations(numbers, 6)))
        for comb in combis:
            print(f'{comb}\n')
        print('\n')