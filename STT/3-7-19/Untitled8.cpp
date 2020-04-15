#include<stdio.h>
int main()
{
	int i,j,k,l,m,n;
	printf("Enter n value");
	scanf("%d",&n);
	for(i=1;i<=2*n-1;i++)
	{
		k=i<=n?i:n-(i%n);
		for(j=1;j<=k;j++)
		{
			printf("*");
		}
		for(l=1;l<=2*(n-k);l++)
		{
			printf(" ");
		}
		for(m=1;m<=k;m++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}
