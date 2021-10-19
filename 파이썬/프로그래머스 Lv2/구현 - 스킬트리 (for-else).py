def solution(skill, skill_trees):
    answer = len(skill_trees)
    for sk in skill_trees:
        tree = [s for s in skill]   # 스킬 스택 생성
        for c in sk:    # 스킬 하나씩 조회
            if c in tree:   # 스킬 스택에 있으면
                if c == tree[0]:    # 첫번째 스택일 경우 pop
                    tree.pop(0)
                else:       # 첫번째 스택이 아닐 경우 답이 아님
                    answer -= 1
                    break
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))

# 노가다 답안
def solution(skill, skill_trees):
    result = 0

    for tree in skill_trees:
        cnt = 0
        flag = 0
        for now_skill in tree:
            for i in range(len(skill)):
                if now_skill == skill[i]:
                    if i > cnt:
                        flag = 1
                        break
                    else:
                        cnt += 1
            if flag == 1:
                break
            if now_skill == tree[len(tree)-1]:
                result += 1
    return result


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))


# 모범 답안
# for-else : break 걸리지 않고 끝가지 수행 시 else문 수행
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
