def solution(n):
    answer = 0
    if n%2 :
        answer = (n//2 +1)*(n//2+1)
    else:
        for i in range(n):
            if (i+1)%2==0: answer += (i+1)*(i+1) 
    return answer