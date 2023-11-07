# 1922 네트워크 연결
# 69064KB / 628ms

import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

g = [[] for _ in range(n+1)]
vi = [False for _ in range(n+1)]
sol = 0

# 모든 간선정보 입력
for i in range(m):
    a,b,c = map(int,input().split())
    g[a].append((c,b))
    g[b].append((c,a))

q = []
heapq.heappush(q, (0,1))

def func():
    global sol
    while q:
        # 현재 q에서 최소 비용과 최소 비용의 위치를 빼냄 
        x, now = heapq.heappop(q)
        # 방문하지 않았을 때
        if vi[now] == False:
            # 방문처리
            vi[now] = True
            # 최소비용을 더함
            sol += x
            # 현재 위치의 정보들을 q에 넣음
            for nx, ny in g[now]:
                heapq.heappush(q, (nx, ny))
    return sol

print(func())

'''
g

[[], 
[(5, 2), (4, 3)], 
[(5, 1), (2, 3), (7, 4)], 
[(4, 1), (2, 2), (6, 4), (11, 5)], 
[(7, 2), (6, 3), (3, 5), (8, 6)], 
[(11, 3), (3, 4), (8, 6)], [(8, 4), (8, 5)]]
'''