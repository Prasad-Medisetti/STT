#include<stdio.h>
int main()
{
	int i,n;
	printf("Enter n value");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		for(int j=i;j<=n;j++)
		{
			printf("*");
		}
		for(int k=1;k<=2*(i-1);k++)
		{
				printf(" ");
		}
		for(int l=i;l<=n;l++)
		{
				printf("*");
		}
		printf("\n");
	}
	return 0;
}
