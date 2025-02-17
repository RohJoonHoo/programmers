def solution(numbers):
    answer = 0
    numbers.sort()
    answer = numbers[-2]*numbers[-1]
    return answer