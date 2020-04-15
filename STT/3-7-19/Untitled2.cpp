#include<stdio.h>
int main()
{
	int i,n;
	printf("Enter n value");
	scanf("%d",&n);
	for(i=n;i>=1;i--)
	{
		for(int j=i;j>=1;j--)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}
