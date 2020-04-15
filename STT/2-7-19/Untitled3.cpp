#include<stdio.h>
int main()
{
	int i,j;
	for(i=10,j=1;i>0&&j<=10;i++,j--)
	{
		printf("%2d%2d\n",j,i);
	}
}
