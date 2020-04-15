#include<stdio.h>
int main()
{
int i,a[5]={1,2,3,4,5};
int *p;
// p=a;
for(i=0;i<5;i++)
printf("\n%d ",a[i]);
printf("\n...........................................\n");
for(i=0;i<5;i++)
{
printf("\n%d ",*p);
p++;
}
return 0;
}
