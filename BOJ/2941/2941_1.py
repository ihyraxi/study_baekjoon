'''
 메모리: 30864 KB, 시간: 80 ms
 2022.03.23
 by Alub
'''
c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
w = input()
for i in c :
    w = w.replace(i, '*')
print(len(w))