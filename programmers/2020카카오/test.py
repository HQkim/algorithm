w = '(())'
num_stack = 0
split_num = len(w)

for i in range(len(w)):
    if w[i] == '(':
        num_stack += 1
    else:
        num_stack -= 1

    if num_stack == 0:
        split_num = i
        break

u = w[:split_num+1]
v = w[split_num+1:]

print(u, v)
print(v)

print(w[5:])