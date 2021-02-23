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
