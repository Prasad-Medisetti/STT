#include<stdio.h>
int main()
{
	int i,n;
	printf("Enter n value");
	scanf("%d",&n);
	for(i=n;i>=1;i--)
	{	for(int k=(n-i);k>=1;k--)
		{
				printf(" ");
		}
			for(int j=n;j>
			=i;j--)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}
