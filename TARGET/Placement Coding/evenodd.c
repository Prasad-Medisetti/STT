#include<stdio.h>
void evenodd(int arr[], int n) {
	int even[n], odd[n], i,e=0,o=0;
	for (i=0;i<n;i++)
	{
		if (arr[i]%2==0)
			even[e++]=arr[i];
		else
			odd[o++]=arr[i];
	}
	printf("\nEVEN \n");
	for (i=0;i<e;i++)
	{
		printf("%d ",even[i]);
	}
	printf("\nODD \n");
	for (i=0;i<o;i++)
	{
		printf("%d ",odd[i]);
	}
}
void main() {
	int n, i;
	scanf("%d",&n);
	int arr[n];
	for (i=0;i<n;i++)
	{
		scanf("%d",&arr[i]);
	}
	printf("\n");
	for (i=0;i<n;i++)
	{
		printf("%d ",arr[i]);
	}
	
	printf("\n");
	evenodd(arr, n);
}
