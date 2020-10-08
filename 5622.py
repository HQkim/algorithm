a = input()

alpha = ["A", "B", "C", "D", 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', "M",
         "N", "O", "P", 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

num = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7,
       7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]

count = []
for i in a:
    ind = alpha.index(i)
    count.append(num[ind])

print(sum(count))
