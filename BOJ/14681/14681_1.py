'''
 메모리: 30864 KB, 시간: 72 ms
 2022.02.27
 by Alub
'''
x= int(input())
y= int(input())

if x > 0 and y > 0 :
    print('1')
elif x < 0 and y > 0 :
    print('2')
elif x < 0 and y < 0 :
    print('3')
else:
    print('4')
