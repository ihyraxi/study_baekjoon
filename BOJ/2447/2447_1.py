'''
 메모리: 40208 KB, 시간: 84 ms
 2022.02.26
 by Alub
'''
import sys

sys.setrecursionlimit(10**6)

def star(n):
    if n == 1:
        return ['*']
    stars = star(n//3)
    L = []

    for S in stars:
        L.append(S*3)
    for S in stars:
        L.append(S+' '*(n//3)+S)
    for S in stars:
        L.append(S*3)
    return L

n = int(sys.stdin.readline().strip())
print('\n'.join(star(n)))