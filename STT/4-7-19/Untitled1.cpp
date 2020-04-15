#include<stdio.h>
#include<math.h>
int main()
{
	int i,n=3,x=2,sum=1,k=1;
	for(i=1;i<=n;i++)
	{
		k=i*k;
		sum=sum+(pow(x,i)/k);
	}
	printf("%d",sum);
	return 0;
}
