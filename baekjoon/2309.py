import sys
from itertools import combinations

input = sys.stdin.readline

if __name__ == "__main__":
    heights = [int(input()) for _ in range(9)]
    heights_comb = list(combinations(heights, 7))

    for comb in heights_comb:
        if sum(comb) == 100:
            comb = list(comb)
            comb.sort()
            for i in comb:
                print(i)
            break
