'''
 메모리: 30860 KB, 시간: 88 ms
 2022.03.29
 by Alub
'''
t=int(input())

for i in range(t):
    k=int(input())
    n=int(input())
    zero=[x for x in range(1, n+1)]
    
    for j in range(k):
        for l in range(1, n):
            zero[l]+=zero[l-1]
            
    print(zero[-1])