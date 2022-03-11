'''
 메모리: 30864 KB, 시간: 72 ms
 2022.03.11
 by Alub
'''
a = []
for i in range(10):
    n = int(input())
    a.append(n % 42)
a = set(a)
print(len(a))