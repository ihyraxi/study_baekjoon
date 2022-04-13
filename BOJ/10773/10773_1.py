'''
 메모리: 31620 KB, 시간: 3756 ms
 2022.04.13
 by Alub
'''
n = int(input())
zero = []
for i in range(n):
    nn = int(input())
    if nn == 0:
        zero.pop()
    else:
        zero.append(nn)
print(sum(zero))