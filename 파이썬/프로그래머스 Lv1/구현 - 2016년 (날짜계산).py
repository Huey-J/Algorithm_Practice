def solution(a, b):
    days = ['FRI','SAT', 'SUN','MON','TUE','WED','THU']
    day_cnt = 0
    for i in range(1, a):
        if i == 1 or i == 3 or i == 5 or i==7 or i==8 or i==10 or i == 12:
            day_cnt += 31
        if i == 2 :
            day_cnt += 29
        if i == 4 or i == 6 or i==9 or i==11:
            day_cnt += 30
    day_cnt += b - 1
    return days[day_cnt % len(days)]

print(solution(5, 24))