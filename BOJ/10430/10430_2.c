/**
* 메모리: 1112 KB, 시간: 0 ms
* 2022.05.17
* by Alub
*/
#include<stdio.h>
int main(void){
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    printf("%d\n",(a+b)%c);
    printf("%d\n",((a%c)+(b%c))%c);
    printf("%d\n",(a*b)%c);
    printf("%d\n",((a%c)*(b%c))%c);
    return 0;
}