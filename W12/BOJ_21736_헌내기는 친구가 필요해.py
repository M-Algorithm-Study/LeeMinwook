# 21736_헌내기는 친구가 필요해
# 39520KB / 420ms

from collections import deque

n, m = map(int, input().split())
campus = [list(input().rstrip()) for _ in range(n)]
d = [(1,0), (0,1), (-1,0), (0,-1)]

# 도연이 위치 저장
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            sx, sy = i, j

def bfs(x, y):
    vi = [[0] * m for _ in range(n)]
    q = deque([(x, y)])
    vi[x][y] = 1
    cnt = 0

    while q:
        x, y = q.popleft()

        # 4방향 탐색
        for dx,dy in d:
            nx, ny = x+dx, y+dy

            # 캠퍼스 범위 안, 벽이 아닐 때, 방문한 곳이 아닐 때
            if 0 <= nx < n and 0 <= ny < m and campus[nx][ny] != 'X' and not vi[nx][ny]:
                vi[nx][ny] = 1
                q.append((nx, ny))

                # 사람이면 +1
                if campus[nx][ny] == 'P':
                    cnt += 1

    return cnt

# bfs 실행 후 cnt 저장
sol = bfs(sx, sy)

# 찾은 사람이 0이면 TT출력, 반대면 cnt 출력
print('TT') if sol == 0 else print(sol)