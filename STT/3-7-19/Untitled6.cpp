#include<stdio.h>
int main()
{
	int i,j,k,l,n;
	printf("Enter n value");
	scanf("%d",&n);
	for(i=1;i<=2*n-1;i++)
	{
		k=i<=n?i:n-(i%n);
		for(l=1;l<=n-k;l++)
		{
			printf(" ");
		}
		for(j=1;j<=k;j++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}
