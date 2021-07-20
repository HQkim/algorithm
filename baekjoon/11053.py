# 백준 11053번 가장 긴 증가하는 부분

import sys

def input_N_and_A():
    input = sys.stdin.readline
    length_of_sequence = int(input())
    sequence = list(map(int, input().rstrip().split()))
    return (length_of_sequence, sequence)

def length_of_longest_increasing_subsequence(length_of_sequence, sequence):
    dp = [1] * length_of_sequence
    for i in range(1, length_of_sequence):
        smaller_index_list = []
        for j in range(i-1 , -1, -1):
            if sequence[i] > sequence[j]:
                smaller_index_list.append(j)
        
        if smaller_index_list:
            max_value = 0
            for k in smaller_index_list:
                if dp[k] > max_value:
                    max_value = dp[k]
            dp[i] = max_value + 1
    return max(dp)

def main():
    length_of_sequence, sequence = input_N_and_A()
    answer = length_of_longest_increasing_subsequence(length_of_sequence ,sequence)    
    print(answer)

main()