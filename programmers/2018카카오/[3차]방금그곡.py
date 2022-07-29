# programmers 2018카카오블라인드 [3차]방금그곡

def solution(m, musicinfos):
    answer = ''
    candidate = []
    d_r = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a'}
    for k, v in d_r.items():
        if k in m:
            m = m.replace(k, v)

    for music in musicinfos:
        start, end, title, melody = music.split(",")
        for k,v in d_r.items():
            if k in melody:
                melody = melody.replace(k, v)
        time = convert_time(end) - convert_time(start)
        real_melody = melody*(time // len(melody)) + melody[:time % len(melody)]
        if m in real_melody:
            candidate.append((title, time))
    
    if not candidate:
        return "(None)"

    candidate = list(enumerate(candidate))
    candidate.sort(key=lambda x: (-x[1][1], x[0]))
    answer = candidate[0][1][0]

    return answer

def convert_time(time):
    h, m = time.split(":")
    result = int(h)*60 + int(m)
    return result

solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])