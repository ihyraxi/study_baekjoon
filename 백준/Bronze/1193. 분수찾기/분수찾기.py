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