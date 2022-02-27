'''
 메모리: 30864 KB, 시간: 68 ms
 2022.02.27
 by Alub
'''
a = int(input())
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print(1)
else:
    print(0)