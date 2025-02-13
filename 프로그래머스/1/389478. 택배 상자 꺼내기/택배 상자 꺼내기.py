def solution(n, w, num):
    answer = 0
    
    total_floor = (n - 1) // w + 1
    
    target_floor = (num-1) //w 
    target_col = w - (num -1) % w if target_floor % 2 else (num-1) % w + 1
    
    if n % w != 0:
        if total_floor % 2:
            if target_col > (n%w) : total_floor -= 1 
        else:
            if target_col <= w - (n % w) : total_floor -= 1
            
    answer = total_floor - target_floor
        
    return answer