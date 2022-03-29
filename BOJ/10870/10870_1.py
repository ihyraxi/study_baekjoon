'''
 메모리: 30864 KB, 시간: 68 ms
 2022.03.29
 by Alub
'''
n=int(input())
def fbn(n):
    if n<=1:
        return n
    return fbn(n-1)+fbn(n-2)
print(fbn(n))