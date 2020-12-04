x, y = map(int, input().split())

days = 0
months = []
for i in range(1, x + 1):
    months.append(i)

for i in range(len(months)):
    month = months[i]
    if i == len(months) - 1:
        break
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days += 31
    elif month in [4, 6, 9, 11]:
        days += 30
    else:
        days += 28

days += y - 1

mod = days % 7

if mod == 0:
    print("MON")
elif mod == 1:
    print("TUE")
elif mod == 2:
    print("WED")
elif mod == 3:
    print("THU")
elif mod == 4:
    print("FRI")
elif mod == 5:
    print("SAT")
else:
    print("SUN")
