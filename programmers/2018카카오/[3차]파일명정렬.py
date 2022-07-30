# programmers 2018카카오블라이든 [3차]파일명 정렬

## --코드--
def solution(files):
    answer = []

    arr = []
    for i in range(len(files)):
        file = files[i]
        head, number = split_file(file)
        arr.append((file, head, number, i))
    
    arr.sort(key=lambda x: (x[1].lower(), int(x[2]), x[3]))
    answer = [a[0] for a in arr]

    return answer


def split_file(file):
    number_start = 0
    for i in range(len(file)):
        if file[i].isdigit():
            number_start = i
            break
    
    tail_start = 0
    for i in range(number_start, len(file)):
        if not file[i].isdigit():
            tail_start = i
            break
    
    if tail_start == 0:
        tail_start = len(file)

    return file[:number_start], file[number_start:tail_start]


# solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
# solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])
solution(["O00321", "O49qcGPHuRLR5FEfoO00321"])

## --소감--
# isdigit()활용하니 편리하다.
# 숫자로 끝나느 파일명에서 tail_start를 잘못잡아서 시간이 좀 걸렸다.