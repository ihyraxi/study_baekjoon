'''
 메모리: 30864 KB, 시간: 1432 ms
 2022.04.02
 by Alub
'''
n = int(input())
m=2
while n != 1:
    if n % m == 0:
        n = n / m
        print(m)
    else: 
        m += 1