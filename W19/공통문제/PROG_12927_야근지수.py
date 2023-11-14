import heapq

def solution(n, works):
    # 예 #3 처럼 남은 시간보다 작업량이 적으면 0을 출력
    if n >= sum(works):
        return 0
    
    # heapq은 최소를 꺼내니 음수로 만들어 최대를 꺼냄
    works = [-w for w in works]
    heapq.heapify(works)

    # 남은 시간만큼 반복하여 최댓값을 1씩 깎아줌(음수라 +1)
    for _ in range(n):
        # print(works)
        i = heapq.heappop(works)
        i += 1
        heapq.heappush(works, i)

    # 결괏값에 제곱만큼의 수를 더해줌(음수 제곱은 똑같아서 그대로 진행)
    result = 0
    for i in works:
        result += i ** 2
    
    return result

# print(solution(4, [4, 3, 3]))
# print(solution(1, [2, 1, 2]))
# print(solution(3, [1, 1]))