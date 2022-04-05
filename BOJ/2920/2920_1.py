'''
 메모리: 30864 KB, 시간: 68 ms
 2022.04.05
 by Alub
'''
numbers = list(map(int,input().split()))
if numbers == sorted(numbers):
    print("ascending")
elif numbers == sorted(numbers, reverse=True):
    print("descending")
else:
    print("mixed")