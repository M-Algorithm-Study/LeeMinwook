# 1463 1로 만들기
# 38932KB / 556ms

import sys
input = sys.stdin.readline

n = int(input())
# dp 리스트 생성
dp = [0] * (n + 1)

# 반복문을 통해 최소 연산 횟수를 갱신하며 dp 리스트에 입력
# 3번의 연산 경우의 수 탐색
for i in range(2, n + 1):
    # 1을 빼는 연산을 먼저 하는 이유는 다음 연산에서 비교할 초기값을
    # 갱신해줘야 하기 때문 / 어차피 밑에서 min으로 걸러짐
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        # 2로 나눠지면 2로 나눈 수의 연산횟수 + 1
        # ex) 12면 6의 연산횟수가 2이기 때문에 3
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        # 3으로 나눠지면 3으로 나눈 수의 연산횟수 + 1
        # ex) 9면 3의 연산횟수가 1이기 때문에 2
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])

'''
실패 코드

n = int(input())
t = 0
res = 1e9

def dfs(n, t):
    if n == 1:
        return min(res, t)
    
    if n % 3 == 0:
        return dfs(n // 3, t + 1)
    elif n % 2 == 0:
        return dfs(n // 2, t + 1)
    else:
        return dfs(n - 1, t + 1)

print(dfs(n))
'''