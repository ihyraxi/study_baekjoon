'''
 메모리: 32816 KB, 시간: 108 ms
 2022.03.18
 by Alub
'''
s = input().upper()
compress = list(set(s))
count_list = [s.count(i) for i in compress]
 
if count_list.count(max(count_list)) > 1:
    print('?')
else:
    print(compress[count_list.index(max(count_list))])
