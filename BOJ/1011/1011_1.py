'''
 메모리: 30864 KB, 시간: 1180 ms
 2022.03.16
 by Alub
'''
t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    distance = y - x
    count = 0 
    move = 1 
    move_plus = 0  
    while move_plus < distance :
        count += 1
        move_plus += move  
        if count % 2 == 0 :
            move += 1  
    print(count)