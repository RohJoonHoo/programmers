def solution(num_list):
    answer = 0
    mul1 = 1
    add1 = 0
    for i in range(len(num_list)):
        mul1 *= num_list[i]
        add1 += num_list[i]
    if mul1 < add1*add1 : answer = 1
    return answer