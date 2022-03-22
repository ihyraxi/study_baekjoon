'''
 메모리: 30860 KB, 시간: 72 ms
 2022.03.22
 by Alub
'''
d = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
r = 0
for j in range(len(a)):
    for i in d:
        if a[j] in i:
            r += d.index(i)+3
print(r)
