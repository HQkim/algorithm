h, m = map(int, input().split())
t = 60*h+m
t_c = t-45

if t_c >= 0:
    print(t_c//60, t_c % 60)
else:
    t_m = t_c+24*60
    print(t_m//60, t_m % 60)
