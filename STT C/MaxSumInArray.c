#include <stdio.h>
int main()
{
	int n,i,sum=0,max=0,l,h,j;
	printf("Enter no.of Elements:\n");
	scanf("%d",&n);
	int a[n];
	printf("Enter %d Elements seperated by spaces:\n",n);
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	for(i=0;i<n;i++)
	{
		if(a[i] < 0)
		{
			sum = 0;
			continue;
		}
		sum += a[i];
		if(max < sum)
		{
			max = sum;
			h=i;
		}
	}	
	printf("Possible Maximum Sum is %d by adding the elements from %d to %d.",max,l+1,h+1);
	return 0;
}
