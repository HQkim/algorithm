# programmers lv2 멀쩡한 사각형
def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a%b)


def solution(w,h):
    answer = 1

    if w == h:
        return w**2 - w

    gcd = get_gcd(w, h)
    w_gcd = w // gcd
    h_gcd = h // gcd

    answer = w*h - (h_gcd + w_gcd - 1) * gcd
    
    return answer

print(solution(8, 12))
