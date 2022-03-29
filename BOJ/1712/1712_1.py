'''
 메모리: 30860 KB, 시간: 68 ms
 2022.03.29
 by Alub
'''
a, b, c = map(int, input().split())

if b>=c:
    print(-1)
    
else:
    print(int(a/(c-b)+1))