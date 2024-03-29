array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    result = []
    for command in commands:
        tmp = array[command[0]-1:command[1]]
        tmp.sort()
        result.append(tmp[command[2]-1])
    return result