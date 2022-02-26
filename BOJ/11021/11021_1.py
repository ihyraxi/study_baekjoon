'''
 메모리: 30864 KB, 시간: 80 ms
 2022.02.26
 by Alub
'''
n=int(input())
for i in range(1, n+1):
    A, B = map(int,input().split())
    print(f"Case #{i}: {A+B}")