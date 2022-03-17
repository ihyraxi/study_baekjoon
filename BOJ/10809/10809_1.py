'''
 메모리: 30864 KB, 시간: 72 ms
 2022.03.17
 by Alub
'''
word = input()
a = list(range(97,123))
for x in a :
    print(word.find(chr(x))) 