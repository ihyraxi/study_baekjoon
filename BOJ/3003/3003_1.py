'''
 메모리: 30864 KB, 시간: 68 ms
 2022.03.04
 by Alub
'''
a = [1, 1, 2, 2, 2, 8]
b = list(map(int, input().split()))
for i in range(6):
    print(a[i]-b[i], end=' ')