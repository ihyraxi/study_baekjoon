'''
 메모리: 30860 KB, 시간: 76 ms
 2022.03.13
 by Alub
'''
for _ in range(int(input())):
    n, *a = (int(x) for x in input().split())
    m = sum(a) / n 
    m = sum(x > m for x in a) / n 
    print(f'{m * 100:.3f}%')
