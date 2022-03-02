'''
 메모리: 30860 KB, 시간: 68 ms
 2022.03.02
 by Alub
'''
a, b = map(int, input().split())
people = list(map(int, input().split()))
party = a * b
for i in people:
    print(i - party, end=' ')