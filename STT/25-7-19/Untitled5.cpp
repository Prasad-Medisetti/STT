#include<stdio.h>
int sum(int);
int main()
{
	int n,s=0;
	scanf("%d",&n);
	s=sum(n);
	printf("%d",s);
	return 0;
}
int sum(int n)
{
	int x;
	if (n==1)
	return n;
	else
	x=n+sum(n-1);
	return x;
}
