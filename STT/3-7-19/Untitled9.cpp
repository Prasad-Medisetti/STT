#include<stdio.h>
int main()
{
	int i,j,k,l,n;
	printf("Enter n value");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		for(l=1;l<=n-i;l++)
		{
			printf(" ");
		}
		for(j=1;j<=2*i-1;j++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}
