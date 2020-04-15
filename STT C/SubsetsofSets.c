#include <stdio.h>
int SubStrings(int*,int);
int main()
{
	int i,n,count;
	printf("Enter number of elements in the Set:\n");
	scanf("%d",&n);
	int s[n];
	printf("Enter elements in the Set:\n");
	for(i=0;i<n;i++)
		scanf("%d",&s[i]);
	count = SubStrings(s,n);
	printf("\nNumber of SubSets : %d",count);
	return 0;
}
int SubStrings(int *s,int n)
{
	int i,j,k,l,c=0;
	printf("Subsets are :\n");
	for(i=0;i<n;i++)
	{
		for(j=0;j<n-i;j++)
		{
			k=i+j;
			for(l=j;l<=k;l++)
				printf("%d ",s[l]);
			printf("\n");
			c++;		 	
		}
	}
	return c;
}
