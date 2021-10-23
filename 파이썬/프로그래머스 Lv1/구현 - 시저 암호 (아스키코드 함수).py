def solution(s, n):
    result = ""
    for c in s:
        if c == ' ':
            result += c
        elif ord('A') <= ord(c) <= ord('Z'):
            changed = ord(c) + n
            if ord('Z') < changed:
                changed = changed - ord('Z') + ord('A') - 1
            result += chr(changed)
        else:
            changed = ord(c) + n
            if ord('z') < changed:
                changed = changed - ord('z') + ord('a') - 1
            result += chr(changed)
    return result


s = "z"
n = 1
print(solution(s, n))
