'''
 메모리: 30860 KB, 시간: 68 ms
 2022.03.01
 by Alub
'''
a = int(input())
b = int(input())
c = int(input())
result = list(str(a*b*c))
for i in range(10):
    print(result.count(str(i)))
