/**
* 메모리: 1112 KB, 시간: 0 ms
* 2022.05.17
* by Alub
*/
#include<stdio.h>
int main(void)
{
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\n", a*(b%10));
    printf("%d\n", a*(b%100/10));
    printf("%d\n", a*(b/100));
    printf("%d\n", a*b);
    return 0;
}