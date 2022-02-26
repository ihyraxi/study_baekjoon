'''
 메모리: 151508 KB, 시간: 920 ms
 2022.02.26
 by Alub
'''
import sys
from bisect import bisect_left

n = int(input())
array = [*map(int, input().split())]
stack = [array[0]]

for i in array:
    if stack[-1] < i:
        stack.append(i)
    else:
        stack[bisect_left(stack, i)] = i

print(len(stack))