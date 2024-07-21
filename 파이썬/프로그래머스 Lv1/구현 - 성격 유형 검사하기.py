def solution(survey, choices):
    score_list = {'A': 0, 'N': 0, 'C': 0, 'F': 0, 'M': 0, 'J': 0, 'R': 0, 'T': 0}

    for i in range(0, len(survey)):
        if choices[i] < 4:
            score_list[survey[i][0]] += 4 - choices[i]
        else:
            score_list[survey[i][1]] += choices[i] - 4

    print(score_list)

    answer = ""
    answer += 'T' if score_list['R'] < score_list['T'] else 'R'
    answer += 'F' if score_list['C'] < score_list['F'] else 'C'
    answer += 'M' if score_list['J'] < score_list['M'] else 'J'
    answer += 'N' if score_list['A'] < score_list['N'] else 'A'

    a = []
    a.insert('s')

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))    # "TCMA"
print(solution(["TR", "RT", "TR"], [7, 1, 3]))                      # "RCJA"
