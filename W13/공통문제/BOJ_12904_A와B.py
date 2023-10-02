# 12904 A와B
# 31380KB / 56ms

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

# 속도 줄이기 위해 미리 길이 저장
len_S = len(S)
len_T = len(T)

def dfs(T, len_T):
    # S로 T를 만들었으면 1을 출력 후 종료
    if S == T: print(1); sys.exit()
    # S가 T보다 길이가 길어지면 만들 수 없으니 새로운 조합 시작
    if len_T < len_S: return

    # 마지막 문자가 A면
    if T[-1] == 'A':
        # 문자열 뒤 A를 제거 후 재귀
        dfs(T[:-1], len_T - 1)
    # 마지막 문자가 B면
    if T[-1] == 'B':
        # 문자열 뒤 B를 제거 후 뒤집고 재귀
        dfs(T[:-1][::-1], len_T - 1)

# t와 lt로 dfs 실행
dfs(T, len_T)
# sys.exit()로 종료되지 않았으면 바꿀 수 없으니 0 출력
print(0)
