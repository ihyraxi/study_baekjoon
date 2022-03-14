'''
 메모리: 30864 KB, 시간: 76 ms
 2022.03.14
 by Alub
'''
num = int(input())
count = 0

while num >= 0:
  if num % 5 == 0:
    count += int(num // 5)
    print(count)
    break
  num -= 3
  count += 1
else:
  print(-1)