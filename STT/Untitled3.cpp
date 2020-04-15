#include<stdio.h>
void reverse(int *,int);
int main()
{
	int a[]={1,2,3,4,5};
	reverse(a,5);
	return 0;
}
void reverse(int *a,int n)
{
	if(n==0)
	return;
	else
	{
		reverse(a+1,n-1);
		printf("%d ",*a);
		return;
	}
}

