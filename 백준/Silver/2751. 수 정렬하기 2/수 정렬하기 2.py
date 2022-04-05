import sys
num = int(sys.stdin.readline())
l=[]
for i in range(num):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    sys.stdout.write(str(i)+'\n')