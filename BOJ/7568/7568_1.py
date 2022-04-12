'''
 메모리: 30840 KB, 시간: 72 ms
 2022.04.12
 by Alub
'''
num = int(input())
student = []

for _ in range(num):
    w, h = map(int, input().split())
    student.append((w, h))

for i in student:
    rank = 1
    for j in student:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")