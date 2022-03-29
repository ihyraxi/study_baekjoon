'''
 메모리: 30864 KB, 시간: 68 ms
 2022.03.29
 by Alub
'''
x = int(input())

n_list = []
n = 0
count = 0

while count < x:
    n += 1
    count += n

count -= n

if n % 2 == 0:
    i = x - count
    j = n - i + 1
    
else:
    i = n - (x - count) + 1
    j = x - count

print(f'{i}/{j}')