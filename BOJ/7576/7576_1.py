'''
 메모리: 97188 KB, 시간: 3032 ms
 2022.03.25
 by Alub
'''
from collections import deque
import sys

m, n = map(int, sys.stdin.readline().split())
t = [[0] * m for i in range(n)]
queue = deque()
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        t[i][j] = int(line[j])
        if t[i][j] == 1:
            queue.append((i, j))

cnt = 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dr[i]
        ny = y + dc[i]
        if 0 <= nx < n and 0 <= ny < m and t[nx][ny] == 0:
            t[nx][ny] = t[x][y] + 1
            queue.append((nx, ny))

max = -1
check = 0
for i in range(n):
    for j in range(m):
        if t[i][j] > max:
            max = t[i][j]
        if t[i][j] == 0:
            max = 0
            check = 1
            break
    if check == 1:
        break

print(max - 1)