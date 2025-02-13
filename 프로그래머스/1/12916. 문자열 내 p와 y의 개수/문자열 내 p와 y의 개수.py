def solution(s):
    answer = True
    number_p = 0
    number_y = 0
    for i in s:
        if 'p' == i: number_p += 1
        if 'P' == i: number_p += 1
        if 'y' == i: number_y += 1
        if 'Y' == i: number_y += 1
    
    if number_p != number_y :answer = False
    return answer