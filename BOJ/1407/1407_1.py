'''
 메모리: 30864 KB, 시간: 72 ms
 2022.02.26
 by Alub
'''
a, b = map(int, input().split())
def f(num):
    cnt = num
    i = 2
    while i <= num:
        cnt += (num//i)*(i//2)
        i *= 2
    return cnt
print(f(b)-f(a-1))