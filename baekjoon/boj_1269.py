# BOJ 1269 대칭 차집합

N_A, N_B = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A | B)- len(A & B))