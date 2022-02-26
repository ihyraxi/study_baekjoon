'''
 메모리: 30864 KB, 시간: 68 ms
 2022.02.26
 by Alub
'''
calc=input()
try:
    eval(calc.replace("+","&").replace("-","&").replace("/","&").replace("*","&"))
    print(int(eval(calc.replace("/","//"))))
except:print("ROCK")
