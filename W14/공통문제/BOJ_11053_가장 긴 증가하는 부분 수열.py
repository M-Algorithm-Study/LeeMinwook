# 11053 가장 긴 증가하는 부분 수열
# 31256KB / 112ms

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))

# dp 리스트
dp = [0] * n

# 2차원 탐색
for i in range(n):
    for j in range(i):
        # 부분 수열의 끝 부분이 현재보다 크고, 부분 수열의 길이가 더 짧을 때
        # and 이후 코드를 빼면, 수열 중간의 가장 긴 부분을 덮어버릴 수 있음
        if A[i] > A[j] and dp[i] < dp[j]:
            # 부분 수열의 길이를 갱신
            dp[i] = dp[j]
    # 부분 수열 중간의 가장 긴 길이로 갱신했으니 +1을 해줌
    dp[i] += 1
    # print(dp)

# 가장 긴 부분 수열의 길이를 출력
print(max(dp))

'''
예제 입력
[10, 20, 10, 30, 20, 50]

위 print(dp)의 출력 결과
[1, 0, 0, 0, 0, 0]
[1, 2, 0, 0, 0, 0]
[1, 2, 1, 0, 0, 0]
[1, 2, 1, 3, 0, 0]
[1, 2, 1, 3, 2, 0]
[1, 2, 1, 3, 2, 4]
'''