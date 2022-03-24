h,m=map(int,input().split())
if h==0 and m==0:
    print(h+23,m+15)
elif h>0 and h<24 and m<45:
    print(h-1,m+15)
elif h==24 and 45>m:
    print(h-1,m+60)
elif h==0 and m<45:
    print(h+23,m-45+60)
else:
    print(h,m-45)