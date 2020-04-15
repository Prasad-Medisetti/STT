#include <stdio.h>
int main()
{
	int a = 5;
	int *p = &a;
	printf("%p --> %p\n",&a,p);	
	printf("%d --> %d",a,*p);
	return 0;
}
