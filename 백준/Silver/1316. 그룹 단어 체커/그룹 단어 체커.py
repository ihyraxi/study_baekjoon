n = int(input())
result = n
for i in range(0,n):
    w=input()
    for j in range(0,len(w)-1):
        if w[j]==w[j+1]:
            pass
        elif w[j] in w[j+1:]:
            result-=1
            break
print(result)