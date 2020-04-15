#include <stdio.h>
void Bin(int);
int main()
{
	int n;
	scanf("%d",&n);
	Bin(n);
	return 0;
}
void Bin(int n)
{
	if(n==0)
		printf("0");
	else
		Bin(n/2);
	printf("%d",n%2);
}
