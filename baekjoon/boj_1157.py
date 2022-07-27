# boj 1157 단어 공부

s = str(input())
s = s.lower()

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
c = []
for i in a:
    c.append(s.count(i))
mymax = max(c)
cnt = c.count(mymax)
if cnt > 1:
    print("?")
else:
    anw = a[c.index(mymax)]
    print(anw.upper())


## 풀이 2 - 이게 왜 시간이 더 오래 걸리는지 모르겠다! 
## 시간복잡도상 이게 더 빠를거 같은데 놓치는게 있나?
# word = input().upper()
# d = dict()

# for w in word:
#     if d.get(w):
#         d[w] += 1
#     else:
#         d[w] = 1

# values = list(d.values())
# max_v = max(values)
# cnt = values.count(max_v)

# if cnt >= 2:
#     print('?')
# else:
#     ind = values.index(max_v)
#     print(f'{list(d.keys())[ind]}')

