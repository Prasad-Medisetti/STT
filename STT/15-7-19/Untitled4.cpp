#include<stdio.h>
int main()
{
	char a[10][100],i,j;
	printf("enter values");
	for(i=0;i<5;i++)
	{
		for(j=0;j<100;j++)
		{
			scanf("%s",a[i][j]);
			if(scanf("%[\n]",a[j]))
			continue;
		}
	}
	for(i=0;i<5;i++)
	{
		for(j=2;j<5;j++)
		{
			printf("%s\n",a[i][j]);
		}
	}
	
	return 0;
}
