#include<stdio.h>
int fact(int);
int main()
{
	int n,f=0;
	scanf("%d",&n);
	f=fact(n);
	printf("%d",f);
	return 0;
}
int fact(int n)
{
	int x;
	if (n==1)
	return n;
	else
	x=n*fact(n-1);
	return x;
}
