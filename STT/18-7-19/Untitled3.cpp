#include<stdio.h>
int main()
{
	int a=5,*p,**q;
	p=&a;q=&p;
//	printf("%p -> %p\n",&a,p);
	printf("%d -> %d -> %d ",a,*p,**q);
	return 0;
}
