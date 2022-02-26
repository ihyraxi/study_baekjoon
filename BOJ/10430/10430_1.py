'''
 메모리: 30864 KB, 시간: 68 ms
 2022.02.26
 by Alub
'''
A, B, C = map(int, input().split())
print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')