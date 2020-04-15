#include<stdio.h>
int main()
{
	int a[5]={1,2,3,4,5};
	int *p,i,sum;
	p=a;
	for(i=0;i<5;i++)
	sum+=*(p+i);
	
	printf("\n%d",sum);
	return 0;
}
