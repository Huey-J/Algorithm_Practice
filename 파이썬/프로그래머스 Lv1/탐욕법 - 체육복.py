#### 내 답안
def solution(n, lost, reserve):
    students = [1] * n
    for i in lost:
        students[i - 1] -= 1
    for i in reserve:
        students[i - 1] += 1

    answer = 0
    for i in range(len(students)):
        if students[i] == 0:  # 잃어버린 학생일 경우
            if i == 0:  # 잃어버린 학생이 맨 처음
                if students[i + 1] == 2:
                    students[i] = 1
                    students[i + 1] = 1
                    answer += 1
            elif i == len(students) - 1:  # 잃어버린 학생이 마지막
                if students[i - 1] == 2:
                    students[i] = 1
                    students[i - 1] = 1
                    answer += 1
            else:  # 잃어버린 학생이 처음 또는 마지막이 아님
                if students[i - 1] == 2:
                    students[i] = 1
                    students[i - 1] = 1
                    answer += 1
                elif students[i + 1] == 2:
                    students[i] = 1
                    students[i + 1] = 1
                    answer += 1
        else:
            answer += 1

    return answer