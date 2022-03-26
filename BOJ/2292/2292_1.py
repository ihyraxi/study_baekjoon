'''
 메모리: 30864 KB, 시간: 72 ms
 2022.03.26
 by Alub
'''
n = int(input())

bee = 1 
cnt = 1

while n > bee:
    bee += 6 * cnt 
    cnt += 1
    
print(cnt)