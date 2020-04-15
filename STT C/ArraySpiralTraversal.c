#include <stdio.h>
int main()
{
	int i,j,x,y,z=1;
	printf("Enter the no.of rows and columns: \n");
	scanf("%d%d",&x,&y);
 	int arr[x][y],k=0,l=0,m=x,n=y;
	printf("Enter the elements:\n");
	for(i=0;i<x;i++)
		for(j=0;j<y;j++)
//			scanf("%d",&arr[i][j]);
			arr[i][j] = z++;
	for(i=0;i<x;i++)
	{
		for(j=0;j<y;j++)
			printf("%d\t",arr[i][j]);
		printf("\n"); 
	}
	while(k < m && l < n)
	{
		for(i=0;i<n;++i)	//	L-R
			printf("%d ",arr[k][i]);
		k++;
		for(i=k;i<m;i++)	//	T-B
			printf("%d ",arr[i][n-1]);
		n--;
		if(k<m)		//	R-L
		{
			for(i=n-1;i>=0;i--)
				printf("%d ",arr[m-1][i]);
			m--;
		}
		if(l<n)		//	L-R
		{
			for(i=m-1;i>k;i--)
				printf("%d ",arr[i][l]);
			l++;	
		}	
	}
//	for(i=0;i<3;i++)
//	{
//		for(j=0;j<3;j++)
//			printf("%d\t",arr[i][j]);
//		printf("\n"); 
//	}
	return 0;
}
