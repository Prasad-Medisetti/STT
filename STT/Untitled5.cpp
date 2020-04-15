#include<stdio.h>
void maxi(int *,int ,int );
int main()
{
	int max,a[]={1,2,3,6,5,4};
	maxi(a,0,6);
	return 0;
}
void maxi(int *a,int max,int n)
{
	if(n==0)
	{
		printf("%d ",max);
	return;
}
	else
	{
		if(max<*a)
		max=*a;
		maxi(a+1,max,n-1);
	}
	
}
