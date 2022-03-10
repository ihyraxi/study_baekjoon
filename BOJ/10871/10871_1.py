'''
 메모리: 30864 KB, 시간: 80 ms
 2022.03.10
 by Alub
'''
n, x = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n):
    if x>a[i]:
        print(a[i],end=" ")