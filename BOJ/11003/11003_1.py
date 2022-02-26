'''
 메모리: 626504 KB, 시간: 7160 ms
 2022.02.26
 by Alub
'''
from collections import deque

N, L = map(int, input().split())
Ai = [*map(int, input().split())]
m = deque()

for i in range(N):
    tmp = Ai[i]

    while m and m[-1] > tmp:
        m.pop()
    m.append(tmp)

    if i >= L and m[0] == Ai[i-L]:
        m.popleft()
    print(m[0], end=' ')