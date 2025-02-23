def solution(num_list):
    answer = []
    even1 = 0
    odd1 = 0
    for i in num_list:
        if i %2 ==0:
            even1 += 1
        else:
            odd1 +=1
    answer.append(even1)
    answer.append(odd1)  
    return answer