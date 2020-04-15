#include<stdio.h>
int main()
{
int a[5]={10,20,30,40,50};
int *p,i;
p=a;
printf("%p - %p ",a,p);
for(i=0;i<5;i++)
    printf("%p ",&a[i]);
    printf("\n");
    for(i=0;i<5;i++)
    printf("%p ",p++);
    p=a;
    for(i=0;i<5;i++)
    {
    printf("\n%d ",*p);
    p++;
}
return 0;
}


