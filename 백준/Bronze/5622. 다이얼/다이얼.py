d = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
r = 0
for j in range(len(a)):
    for i in d:
        if a[j] in i:
            r += d.index(i)+3
print(r)
