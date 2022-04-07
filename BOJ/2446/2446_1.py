'''
 메모리: 30864 KB, 시간: 68 ms
 2022.04.08
 by Alub
'''
n = int(input())

for i in range(n):
    print(" " * i + "*" * ((n - i) * 2 - 1))
    
for i in range(n - 2, -1, -1):
    print(" " * i + "*" * ((n - i) * 2 - 1))