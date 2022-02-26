'''
 메모리: 30864 KB, 시간: 72 ms
 2022.02.26
 by Alub
'''
N = int(input())
Num = list(map(int, input().split()))

if N == 1:
    print(sum(Num)-max(Num))

else:
    sumList = [min(Num[0], Num[5]), min(Num[1], Num[4]), min(Num[2], Num[3])]
    sumList.sort()
    f = (N-2)*(N-2) + (N-1)*(N-2)*4
    s = (N-2)*4 + (N-1)*4
    t = 4

    result = f * sumList[0] + s * sum(sumList[:2]) + t * sum(sumList)
    print(result)