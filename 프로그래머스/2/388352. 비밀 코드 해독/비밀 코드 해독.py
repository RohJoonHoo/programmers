from itertools import combinations

def solution(n, q, ans):
    possible_codes = list(combinations(range(1, n+1), 5))
    answer = 0

    for code in possible_codes:
        is_valid = True
        for j in range(len(q)):
            actual_match = sum(1 for num in q[j] if num in code)
            expected_match = ans[j]

            if actual_match != expected_match:
                is_valid = False
                break

        if is_valid:
            answer += 1

    return answer
