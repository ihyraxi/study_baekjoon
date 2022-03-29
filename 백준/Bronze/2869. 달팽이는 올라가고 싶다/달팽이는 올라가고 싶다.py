import sys
from math import ceil
a, b, v = map(int,sys.stdin.readline().split())
print(ceil((v-b)/(a-b)))