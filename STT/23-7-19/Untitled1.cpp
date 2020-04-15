#include<stdio.h>
int main()
{
	int a[10]={1,2,3};
	printf("%u,%u,%u,%u",a,&a[0],a+1,&a[0]+1);
	return 0;
}
