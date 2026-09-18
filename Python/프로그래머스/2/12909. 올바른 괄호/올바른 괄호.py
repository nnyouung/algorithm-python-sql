def solution(s):
    lst = []
    for i in s:
        if i == '(':
            lst.append(i)
        elif i == ')':
            if not lst:
                return False
            lst.pop()

    return not lst