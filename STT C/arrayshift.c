#include<stdio.h>
int main()
{
	int n=10,i,j,shift,temp;
	int a[n];
	int type;
	printf("Enter the elements:");
	for(i=0;i<10;i++)
	 scanf("%d",&a[i]);
    printf("Enter the shift size and type of rotation(0-left 1-right):");
    scanf("%d%d",&shift,&type);
     printf("Before shifting:");
	for(i=0;i<10;i++)
	 printf("%d ",a[i]);
	 if(type==1)
	 {
	    for(i=0;i<shift;i++)
	    {
	    	temp=a[n-1];
	    	for(j=n-2;j>=0;j--)
	    	{
	    		a[j+1]=a[j];
			}
			a[0]=temp;
		}
	}
	else
	{
		for(i=0;i<shift;i++)
	    {
		    temp=a[0];
	    	for(j=0;j<=n-1;j++)
	    	{
	    		a[j]=a[j+1];
			}
			a[n-1]=temp;
		}
	}
	 printf("\nAfter shifting:");
		for(i=0;i<10;i++)
	 printf("%d ",a[i]);
}
