'''
 메모리: 30864 KB, 시간: 80 ms
 2022.03.29
 by Alub
'''
t=int(input())

for i in range(t):
    h, w, n=map(int,input().split())
    
    num = n // h + 1
    floor = n % h
    
    if n % h == 0:
        num = n // h
        floor = h
    
    print(f'{floor*100+num}')