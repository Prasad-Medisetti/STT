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
	n=x+y;
	for(i=0;i<x;i++)
	{
		u[i]=a[i];
	}
	for(i=0;i<y;i++)
	{
		u[x+i]=b[i];
	}
	for(i=0;i<n;i++)
	{
		printf("%d  ",u[i]);
	}
	return 0;
	
}
