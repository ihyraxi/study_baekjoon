n = int(input())
nn = map(int, input().split())
f = 0

for i in nn:
    x = 0
    if i > 1 :
        for j in range(2, i):
            if i % j == 0:
                x += 1
        if x == 0:
            f += 1
            
print(f)
 