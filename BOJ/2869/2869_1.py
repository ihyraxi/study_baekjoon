'''
 메모리: 32976 KB, 시간: 72 ms
 2022.03.29
 by Alub
'''
import sys
from math import ceil
a, b, v = map(int,sys.stdin.readline().split())
print(ceil((v-b)/(a-b)))