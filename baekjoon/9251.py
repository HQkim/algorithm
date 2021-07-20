import sys

input = sys.stdin.readline

word_a = input().strip()
word_b = input().strip()

def lcs_calculator(word_a, word_b):
    length_word_a = len(word_a)
    length_word_b = len(word_b)

    matrix = [[0] * (length_word_b + 1) for _ in range(length_word_a + 1)]

    for i in range(1, length_word_a + 1):
        for j in range(1, length_word_b + 1):
            if word_a[i-1] == word_b[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    return matrix[-1][-1]

lcs_length = lcs_calculator(word_a, word_b)
print(lcs_length)

