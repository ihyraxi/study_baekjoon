n = int(input())
zero = []
for i in range(n):
    nn = int(input())
    if nn == 0:
        zero.pop()
    else:
        zero.append(nn)
print(sum(zero))