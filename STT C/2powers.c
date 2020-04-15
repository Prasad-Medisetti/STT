#include<stdio.h>
#include <math.h>
void main()
{
//	int n,i,c=0;
//	printf("Enter a number:");
//	scanf("%d",&n);
//	for(i=0;i<=n;i++)
//	{
//		if(n==pow(2,i))
//		{
//			c++;
//			break;
//		}
//		
//	}
//	if(c==1)
//	 printf("Is a power of 2");
//	 else
//	 printf("jkgzfb");


 	 	int n,i,a=1,c=0;
	printf("Enter a number:");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		a=2*a;
		if(n==a||n==1)
		{
			c++;
			break;
		}
		
	}
	if(c==1)
	 printf("Is a power of 2");
	 else
	 printf("Not a power of 2");
   
}
