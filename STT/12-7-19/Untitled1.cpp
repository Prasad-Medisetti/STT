#include<stdio.h>
int main()
{
	int a[10],i,j=0,k=0,n,even[10],odd[10];
	printf("enter n");
	scanf("%d",&n);
	printf("enter values");
	scanf("%d",&a);
	for(i=0;i<n;i++)
	{
		if(a[i]%2==0)
		{
			even[j]=a[i];
			j++;
		}
		else
		{
			odd[k]=a[i];
			k++;
		}
		printf("%d",a);
	}return 0;
}
