'''
 메모리: 30860 KB, 시간: 72 ms
 2022.03.14
 by Alub
'''
n = int(input())
result = 1
if n > 0:
    for i in range(1, n+1):
        result *= i
print(result)