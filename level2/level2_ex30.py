#30 방금그곡

def change(m):
    while True:
        if '#' in m:
            idx = m.find('#')
            m = m.replace(m[idx-1]+'#',m[idx-1].lower())
        else:
            break
    return m
def solution(m, musicinfos):
    answer = ('(None)', None)
    m = change(m)
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        start_h, start_m, end_h, end_m = map(int, start.split(':') + end.split(':'))
        time = 60*(end_h-start_h) + (end_m-start_m)
        melody = change(melody)
        melody_played = (melody*time)[:time]
        if m in melody_played:
            if (answer[1] == None) or (time > answer[1]):
                answer = (title, time)
    return answer[0]