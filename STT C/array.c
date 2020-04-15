#include<stdio.h>
int main()
{
	int n,i;
//	printf("Enter size : \t");
//	scanf("%d",&n);
	int a[10]={1,2,3,4,5,6,7,8,9,10},b[10]={0},c[10] = {0};
	for(i=0;i<10;i++)
	{
		if(i<5)
		{
			b[i]=a[i];
		}
		else
		{	
			c[i-5]=a[i];
		}
	}	
   for(i=0;i<10;i++)
	{	
		printf("a[%2d] : %2d\t",i,a[i]);
		printf("b[%2d] : %2d\t",i,b[i]);
		printf("c[%2d] : %2d\n",i,c[i]);
	}
	return 0;
}
