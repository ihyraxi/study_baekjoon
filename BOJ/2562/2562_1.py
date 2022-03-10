'''
 메모리: 30864 KB, 시간: 72 ms
 2022.03.10
 by Alub
'''
max_n = 0
for i in range(1,10):
    a = int(input())
    if max_n < a:
        max_n = a
        number=i
print(max_n)
print(number)