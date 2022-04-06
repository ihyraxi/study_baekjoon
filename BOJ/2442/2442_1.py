'''
 메모리: 30864 KB, 시간: 72 ms
 2022.04.06
 by Alub
'''
n = int(input())
for i in range(1, n+1):
    print(' ' * (n-i) +'*'*((2*i)-1))