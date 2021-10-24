# # #코드 소문자로 변경
# def changeMusic(music):
#     changed = ""
#     for i in range(len(music)):
#         if music[i] == '#':
#             continue
#         if music[i] == 'C' or music[i] == 'D' or music[i] == 'F' or music[i] == 'G' or music[i] == 'A' or music[i] == 'E':
#             if i != len(music) - 1:
#                 if music[i+1] == '#':
#                     changed += music[i].lower()
#                     i+=1
#                     continue
#         changed += music[i]
#     return changed


# def solution(m, musicinfos):
#     result = []

#     m = changeMusic(m)
#     for index in range(len(musicinfos)):
#         infoList = musicinfos[index].split(',')

#         # 시간 차이 계산
#         startHour, startMin = map(int, infoList[0].split(':'))
#         endHour, endMin = map(int, infoList[1].split(':'))
#         timeDiff = (endHour - startHour) * 60 + endMin - startMin

#         # 전체 음악 추출
#         infoList[3] = changeMusic(infoList[3])
#         nowMusicInfo = ""
#         for i in range(timeDiff):
#             nowMusicInfo += infoList[3][i % len(infoList[3])]

#         # m 찾기
#         foundedIndex = nowMusicInfo.find(m)
#         if foundedIndex != -1:
#             # '#' 검사
#             lastIndex = foundedIndex + len(m)
#             if lastIndex != len(nowMusicInfo):
#                 if nowMusicInfo[lastIndex] != '#':
#                     result.append([index, timeDiff])
#     if len(result) == 0:        # 일치하는 음악이 없음
#         return "(None)"
#     else:
#         maxTimeDiff = 0
#         maxIndex = 0
#         for r in result:
#             if maxTimeDiff < r[1]:
#                 maxTimeDiff = r[1]
#                 maxIndex = r[0]
#         return musicinfos[maxIndex].split(',')[2]

def change(melody):
    melody = melody.replace('A#', 'a').replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')
    return melody

def solution(m, musicinfos):
    m = change(m)
    answer = ('(None)', -1)
    for info in musicinfos:
        startTime, endTime, title, melody = info.split(',')

        # 시간 구하기
        start_h, start_m, end_h, end_m = map(int, startTime.split(':') + endTime.split(':'))
        time = 60 * (end_h - start_h) + (end_m - start_m)
        
        melody = change(melody)
        melody_played = (melody * ((time // len(melody)) + 1))[:time]  # 실제 틀어진 음악

        if m in melody_played:
            if (time > answer[1]):
                answer = (title, time)
    return answer[0]


m = "ACD"
musicinfos = ["12:55,13:05,HELLO,ABC", "13:00,13:4,WORLD,A#C#D#"]
print(solution(m, musicinfos))
