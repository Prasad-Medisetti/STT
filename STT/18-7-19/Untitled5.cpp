#include<stdio.h>
int main()
{
	int a[5]={1,2,3,4,5};
	int (*p)[5];
	p=&a;
   	printf("%p -> %p\n",p,a);
	return 0;
}
