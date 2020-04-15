#include<stdio.h>
int main()
{
 	int i,n,sum=0;
 	printf("Enter the number of elements: ");
 	scanf("%d",&n);
 	int a[n];
 	printf("\nEnter the elements: ");
 	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	for(i=0;i<n;i++)
	{
		a[i] = a[i] + a[i-1];
	}
	  printf("Sum of the elements is :%d ",a[n-1]);
	  printf("\n");
	  for(i=0;i<n;i++)
       printf("%d ",a[i]);	
//    for(i=0;i<n;i++)
//      {
//      	sum=sum+a[i];
//      	a[i]=sum;
//	  }
//	  printf("Sum of the elements is :%d ",sum);
//	  printf("\n");
//	  for(i=0;i<n;i++)
//       printf("%d ",a[i]);
	return 0;
}
