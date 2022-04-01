'''
 메모리: 30864 KB, 시간: 120 ms
 2022.04.01
 by Alub
'''
n = int(input())
m = []
for i in range(n):
    m.append(int(input()))
mm = sorted(m)
for i in range(len(m)):
    print(mm[i])