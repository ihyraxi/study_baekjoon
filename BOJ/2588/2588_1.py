'''
 메모리: 30864 KB, 시간: 68 ms
 2022.02.26
 by Alub
'''
n = int(input())
m = int(input())

print(n * (m%10))
print(n * ((m%100)//10))
print(n * (m//100))
print(n * m)