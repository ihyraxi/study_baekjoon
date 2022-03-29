n=int(input())
def fbn(n):
    if n<=1:
        return n
    return fbn(n-1)+fbn(n-2)
print(fbn(n))