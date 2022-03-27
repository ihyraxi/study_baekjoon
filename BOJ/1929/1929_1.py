'''
 메모리: 30864 KB, 시간: 5632 ms
 2022.03.27
 by Alub
'''
n, m = map(int, input().split())

for i in range(n, m+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)