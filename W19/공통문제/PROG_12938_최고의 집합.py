def solution(n, s):
    answer = []
    
    # d = 원소들의 합을 자연수의 개수로 나눈 몫
    # m = 원소들의 합을 자연수의 개수로 나눈 나머지
    d, m = divmod(s, n)

    # 몫이 0이면 집합을 만들 수 없으니 -1을 출력
    if d == 0:
        return [-1]
 
    # 자연수의 개수 - 나머지 수만큼 몫을 집합에 추가
    for _ in range(n - m):
        answer.append(d)

    # 나머지 수만큼 몫을 집합에 추가 
    for _ in range(m):
        answer.append(d + 1)

    return answer

# print(solution(2, 9))
# print(solution(2, 1))
# print(solution(2, 8))