# 20444 색종이와 가위
# 31256KB / 40ms

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, k = map(int,input().split())

# n이 2^31까지라 이분 탐색
def binary(st, end):
    # 시작이 끝보다 많아지면 만들 수 없으니 NO 출력
    if st > end: return 'NO'
    # 이분탐색 중간값
    mid = (st + end) // 2
    # 총 색종이 조각 수 = (한 방향 + 1) * (반대 방향 + 1)
    sum_mid = (mid + 1) * (n - mid + 1)

    # k와 똑같으면 만들 수 있으니 YES 출력
    if sum_mid == k: return 'YES'
    # k보다 적으면 중간에서 큰 쪽 탐색
    elif sum_mid < k:
        return binary(mid + 1, end)
    # k보다 크면 중간에서 작은 쪽 탐색
    else:
        return binary(st, mid - 1)

# n//2을 한 이유는 아래 설명
print(binary(0, n // 2))

'''
n = 17이라고 쳤을 때
가로 세로 sum_mid
  8   9  9*10 = 90
  7   10 8*11 = 88
  6   11 7*12 = 84
  5   12 6*13 = 78
  4   13 5*14 = 70
  3   14 4*15 = 60
  2   15 3*16 = 48
  1   16 2*17 = 34

중간으로 갈수록 커지고,
중간이 가장 큰 값이기 때문에 반값까지만 탐색
'''