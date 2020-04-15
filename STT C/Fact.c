#include <stdio.h>
int Fact(int n);
int main()
{
	int n,fact=0;
	scanf("%d",&n);
	fact=Fact(n);
	printf("Factorial : %d",fact);
	return 0;
}
int Fact(int n)
{
	int x;
	if(n==1||n==0)
		return 1;
	else
		x=n*Fact(n-1);
	return x;
}
