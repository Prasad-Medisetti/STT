#include<stdio.h>
#include<math.h>
int main()
{
	int n,x[300]={0};
	int i,j,l=0,k=2,count=0;
	printf("Enter no.of elements in the set:\n");
	scanf("%d",&n);
	int a[n];
	printf("Enter elements in the set seperated by spaces:\n");
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	x[0]=a[0];
	x[1]=-2;
	for(i=1;i<n;i++)
	{
		x[k++]=a[i];
		x[k++]=-2;
	  	for(j=0;j<=l;j++)
	  	{
	 		if(x[j]==-2)
	  	  	{
				x[k++]=a[i];
				x[k++]=-2;
  			}
	  	  	else
				x[k++]=x[j];
		}	
	  	x[k]=a[i];
	  	l=k++;
	  	x[k++]=-2;
	} 
	printf("{");
	for(i=0;i<k;i++)
	{
		if(x[i]==-2)
		{
			count++;
		    printf("\b}");
		    printf("\n");
		    if(count<pow(2,n)-1)
				printf("{");
			else
		    	printf("{}");
		}
		else
			printf("%d ",x[i]);
	}
	printf("\nThe number of subsets are: %d",count+1);
	return 0;
}
