#include<stdio.h>
void bin(int);
int main()
{
	int n;
	scanf("%d",&n);
	bin(n);
	return 0;
}
void bin(int n)
{
	if (n==0)
	printf("0");
	else
	bin(n/2);
	printf("%d",n%2);
}
