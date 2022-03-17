'''
 메모리: 30864 KB, 시간: 72 ms
 2022.03.17
 by Alub
'''
def h(num) :
    cnt = 0
    for i in range(1, num+1):
        num_list = list(map(int,str(i)))
        if i < 100:
            cnt += 1
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            cnt += 1 
    return cnt
num = int(input())
print(h(num))