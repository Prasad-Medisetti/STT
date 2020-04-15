#include<stdio.h>
int main()
{
	int n=5,i,temp,ele,pos;
	int a[n];
	printf("Enter the elements:");
	for(i=0;i<n;i++)
	 scanf("%d",&a[i]);
    for(i=0;i<n/2;i++)
    {
    	temp=a[i];
    	a[i]=a[n-1-i];
    	a[n-1-i]=temp;
	}
    
	 printf("\nAfter reversing:");
		for(i=0;i<n;i++)
	 printf("%d ",a[i]);
}
