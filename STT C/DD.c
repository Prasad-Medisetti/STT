#include<stdio.h>
void main()
{
	int i,n,j;
	printf("Enter the number: ");
    scanf("%d",&n);
    j=n;
	for(i=1; i<=2*n-1;i++)  
    {
    	
    	if(i>=n)
    	{
		printf("%d ",j);
		j--;
    	}
    	else
		printf("%d ",i);
	}
}
