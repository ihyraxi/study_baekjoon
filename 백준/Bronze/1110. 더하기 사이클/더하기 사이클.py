num = int(input())
check = num
new = 0
temp = 0
count = 0
while True:
    temp = num//10 + num%10
    new = (num%10)*10 + temp%10
    count += 1
    num = new
    if new == check:
        break
print(count)