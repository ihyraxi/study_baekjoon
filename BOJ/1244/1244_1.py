'''
 메모리: 30840 KB, 시간: 68 ms
 2022.05.18
 by Alub
'''
import sys;input=sys.stdin.readline

n = int(input())
arr = [-3333] + list(map(int, input().split()))  
 
def xy(switch, nn):
    for i in range(nn, n + 1, nn):  
        switch[i] = (switch[i] + 1) % 2
    return switch
 
def xx(switch, nn):
    left, right = nn - 1, nn + 1
    flag = True
 
    try:    #indexError
        while flag:
            if switch[left] == switch[right]:
                left -= 1
                right += 1
            else:
                flag = False
    except:
        pass
 
    for i in range(left + 1, right):   
        switch[i] = (switch[i] + 1) % 2
    return switch
 
student = int(input())
for _ in range(student):
    sex, number = map(int, input().split())
    if sex == 1:
        xy(arr, number)
    else:
        xx(arr, number)
 
for i in range(1, len(arr)):   
    print(arr[i], end=' ')
    if not i % 20:
        print()