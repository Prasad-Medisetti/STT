#include<stdio.h>
void add(int* ,int);
int main()
{
	int a=23,b=23;
	add(&a,b);
	printf("%d, %d ",a,b);
	return 0;
}
void add(int *a,int b)
{
	*a=*a+1;
	b=b+1;
	return;
}
