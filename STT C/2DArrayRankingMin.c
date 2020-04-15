/*
4.	Write a C program to read a two dimensional array of integers, and then find the ranking of the each element in the array as minimum element in the array is taken as 1 and next minimum element in the array as 2 and so on. Now display the rank matrix of the given array.
	Note: Two or more elements are same in the array then rank also be the same for those elements.
	Example:
           Input					Output
     	   10  16    8				2  4  1
	       17  45  	59 				5  6  7		
	        8  11   77 				1  3  8
*/
#include <stdio.h>
int main()
{
	int m,n,i,j;
	printf("Enter a no.of rows & cols of 2D Array:\n");
	scanf("%d%d",&m,&n);
	int a[m][n];
	int rank[m][n]={0},min=0;
	printf("Enter elements of 2D Array:\n");
	for(i=0;i<m;i++)
		for(j=0;j<n;j++)
			scanf("%d",&a[i][j]);
	
	
//	for(i=0;i<m;i++)
//	{
//		for(j=0;j<n;j++)
//			printf("%2d ",a[i][j]);
//		printf("\n");
//	}
	return 0;
}
