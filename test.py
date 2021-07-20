# 1
a = ['h', 'i']
c = ['b', 'y', 'e']
print([*a, 'w', *c])

# 2
lista = list(range(10))
listb = lista[:5]
listc = lista[5:]
print([*listb, *listc])

# 3
numbers = [1, 2, 3, 4, 5, 6]
*a, = numbers
print(*a)

*a, b = numbers
print(*a, '///', b)

a, *b = numbers
print(a, '///', *b)

a, *b, c = numbers
print(a, '/', *b, '/', c)

a, b, *lista, c = numbers

print(a, '/', b, '/', *lista, '/', c)
