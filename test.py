# 순혁이 

# 순혁이 공통
a_com = 5650 + 45000 + 8700

# 현욱이 공통
b_com = 8000

# 현규 공통
c_com = 0

# 현욱 -> 순혁
b_a = 7530 + 6250 + 8700 + 3350

# 현규 -> 순혁
c_a = 1050 + 9200/2

# 순혁 -> 현규
a_c = 22400/2 + 500*35

money_all = (a_com+b_com+c_com)/3
a_sub = -(money_all - a_com) -a_c +c_a +b_a
b_sub = -(money_all - b_com) -b_a
c_sub = -(money_all - c_com) +a_c -c_a

print(a_com)
print(b_com)
