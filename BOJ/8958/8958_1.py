'''
 메모리: 30864 KB, 시간: 80 ms
 2022.03.13
 by Alub
'''
n = int(input())
for i in range(n):
    a = input()
    score = 0
    sum = 0
    for j in a:
        if j == 'O':
            score += 1
        else:
            score = 0
        sum += score
    print(sum)