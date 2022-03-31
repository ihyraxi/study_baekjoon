n = int(input())
m = []
for i in range(n):
    m.append(int(input()))
mm = sorted(m)
for i in range(len(m)):
    print(mm[i])