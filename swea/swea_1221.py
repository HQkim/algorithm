# swea 1221 GNS

for _ in range(10):
    tc = int(input())
    target = input()                # 찾을 문자열
    word = input()                  # 검색할 문장

    target_length = len(target)     # 찾을 문자열의 길이
    word_length = len(word)         # 검색할 문장의 길이

    count = 0
    for i in range(word_length-target_length+1):    # Brute Force 알고리즘
        is_same = True                              # 현재위치에서 찾았을 때 같은지 나타내는 플래그
        for j in range(target_length):
            if target[j] != word[i+j]:              # 같지 않은 요소가 나오면 break
                is_same = False
                break

        if is_same:
            count += 1

    print(f'#{tc} {count}')
