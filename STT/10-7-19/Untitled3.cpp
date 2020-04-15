#include<stdio.h>
int main()
{
	int i,a[10],b[10],u[25],x,y,n,k=0;
	printf("Enter 1st array size");
	scanf("%d",&x);
	printf("Enter 1st array elements");
	for(i=0;i<x;i++)
	scanf("%d",&a[i]);
	printf("Enter 2nd array size");
	scanf("%d",&y);
	printf("Enter 2nd array elements");
	for(i=0;i<y;i++)
	scanf("%d",&b[i]);
	for(i=0;i<n;i++)
	{
		for(int j=0;j<=i;j++)
		{
			if(a[i]==b[j])
			{
				u[j]=b[j];
			}
		}
	}
	for(int j=0;j<n;j++)
	{
		printf("%d  ",u[j]);
	}
	return 0;
	
}
