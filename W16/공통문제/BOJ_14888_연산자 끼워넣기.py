# 14888 연산자 끼워넣기
# 31256KB / 60ms

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
pl, mi, mu, di = list(map(int,input().split()))
mx, mn = -1e9, 1e9

# 각 남은 연산가능한 횟수, 현재 숫자 위치 cnt, 연산한 결괏값
def dfs(pl, mi, mu, di, cnt, t):
    global mx, mn

    # 주어진 숫자 갯수와 현재 숫자 위치가 같거나 커지면 최댓값, 최솟값 갱신
    if cnt >= n:
        mx = max(mx,t)
        mn = min(mn,t)
        return

    if pl: dfs(pl - 1, mi, mu, di, cnt + 1, t + a[cnt])
    if mi: dfs(pl, mi - 1, mu, di, cnt + 1, t - a[cnt])
    if mu: dfs(pl, mi, mu - 1, di, cnt + 1, t * a[cnt])
    if di:
        # 음수 나눗셈은 값이 다르게 나오기 때문에 양수로 바꿔서 연산 후 다시 음수로 변환
        # ex) print(3//2) = 1 / print(-3//2) = -2
        if t < 0:
            dfs(pl, mi, mu, di - 1, cnt + 1, -(-t // a[cnt]))
        else:
            dfs(pl, mi, mu, di - 1, cnt + 1, t // a[cnt])

# 주어진대로 입력, 첫 수를 넣고 시작하니 cnt는 1로 시작, 첫 수 입력
dfs(pl, mi, mu, di, 1, a[0])
print(mx, mn, sep='\n')