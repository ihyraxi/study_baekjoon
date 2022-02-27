'''
 메모리: 30864 KB, 시간: 72 ms
 2022.02.27
 by Alub
'''
score=int(input())
if score >= 90 and score <= 100 :
    print("A")
elif score >= 80 and score <= 89 :
    print("B")
elif score >= 70 and score <= 79 :
    print("C")
elif score >= 60 and score <= 69 :
    print("D")
else :
    print("F")