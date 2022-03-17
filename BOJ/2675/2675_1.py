'''
 메모리: 30860 KB, 시간: 68 ms
 2022.03.17
 by Alub
'''
t = int(input())
for _ in range(t):
    r, s = list(map(str, input().split()))
    r = int(r)
    for i in s:
        print(r*i, end='')
    print()