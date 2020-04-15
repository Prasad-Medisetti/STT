#include<stdio.h>
void main()
{
	int i,n,j;
	printf("Enter the number: ");
    scanf("%d",&n);
	for(i=1;i<= n || j > 0;i++,j--)  
    {
    	
    	if(i<=n)
    	{
    		j=n;
    		printf("%d ",i);
    	}
		else
		printf("%d ",j);
	}
}
