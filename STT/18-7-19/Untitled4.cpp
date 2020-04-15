#include<stdio.h>
int main()
{
	int a=5;
	int *p=&a;
   	printf("%p -> %d\n",p,*p);
   	(*p)++;
   	
	printf("%d -> %d",p,*p);
	return 0;
}
