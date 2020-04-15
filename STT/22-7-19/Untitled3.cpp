#include<stdio.h>
int main()
{
int a[5]={10,20,30,40,50};
int *p,i;
p=a;
for(i=0;i<5;i++)
    printf("%p ",&a[i]);
    printf("\n%p - %p ",(p+i),(i+p));


    return 0;
}

