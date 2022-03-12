'''
 메모리: 30864 KB, 시간: 76 ms
 2022.03.12
 by Alub
'''
a = int(input())
score = list(map(int, input().split()))
up = max(score)
result = 0
for i in range(0,a):
    score[i] = score[i] / up * 100
    result = result + score[i]
result = result / a
print(result)