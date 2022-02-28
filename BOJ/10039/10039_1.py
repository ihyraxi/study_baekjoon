'''
 메모리: 30860 KB, 시간: 68 ms
 2022.02.28
 by Alub
'''
total = 0

for i in range(5):
    score = int(input())

    if score < 40:
        score = 40

    total += score

print(total // 5)
