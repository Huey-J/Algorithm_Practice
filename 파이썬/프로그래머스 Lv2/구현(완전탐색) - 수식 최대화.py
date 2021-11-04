from itertools import permutations


def solution(expression):
    # 리스트 생성
    number_list, symbol_list = [], []
    tmp_number = ""
    for i in range(len(expression)):
        if expression[i] == '-' or expression[i] == '+' or expression[i] == '*':
            number_list.append(tmp_number)
            symbol_list.append(expression[i])
            tmp_number = ""
        else:
            tmp_number += expression[i]
    number_list.append(tmp_number)
    symbol_permutaion_list = list(permutations(list(set(symbol_list))))

    answer = 0
    for permut in symbol_permutaion_list:
        tmp_number_list = [] + number_list
        tmp_symbol_list = [] + symbol_list
        for s in range(len(permut)):
            i = 0
            while True:
                if i >= len(tmp_symbol_list):
                    break
                if tmp_symbol_list[i] == permut[s]:
                    tmp_number_list[i] = str(
                        eval(tmp_number_list[i] + tmp_symbol_list[i] + tmp_number_list[i+1]))
                    tmp_number_list.pop(i+1)
                    tmp_symbol_list.pop(i)
                else:
                    i += 1
        if answer < abs(int(tmp_number_list[0])):
            answer = abs(int(tmp_number_list[0]))
    return answer


print(solution("100-200*300-500+20"))