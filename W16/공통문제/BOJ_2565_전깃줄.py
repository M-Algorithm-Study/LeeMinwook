# 2565 전깃줄
# 31120KB / 44ms

import sys
input = sys.stdin.readline

n = int(input())
# 그림과 같이 나오도록 정렬해서 입력을 받음
a = sorted([list(map(int, input().split())) for _ in range(n)])
dp = [0] * n

# 가장 긴 증가하는 부분 수열 / BOJ_12865
for i in range(n):
    for j in range(i):
        if a[i][1] > a[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

# LIS를 찾았으니 나머지를 빼주면 교차하지 않는 전깃줄을 구할 수 있음
print(n - max(dp))