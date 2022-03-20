'''
 메모리: 30860 KB, 시간: 72 ms
 2022.03.20
 by Alub
'''
a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])
if a > b :
    print(a)
else:
    print(b)
    