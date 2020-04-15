#include<stdio.h>
void main()
{
//	int i, j,n = 5;
//	for(i=0;i <= n; i++)
//	{
//		for(j = 0; j < i; j++)
//			  printf(" *");
//		printf("\n");	  
//	}
/*
 *
 * *
 * * *
 * * * *
 * * * * *
*/

//	int i, j,n = 5;
//	for(i=1;i <= n; i++)
//	{
//		for(j = n; j >= i; j--)
//			  printf(" *");
//		printf("\n");	  
//	}

//	int i, j,k,n = 5;
//	for(i=1;i <= n; i++)
//	{
//		for(j = 1; j <= n-i; j++)
//			  printf(" ");
//	  	for(k = 1; k <= i; k++)
//			    printf("*");
//		printf("\n");	  
//	}
//	
//	
//		int i, j,k,n = 5;
//	for(i=1;i <= n; i++)
//	{
//		for(j = 1; j <= n-i; j++)
//			  printf(" ");
//	  	for(k = 1; k <= i; k++)
//			    printf(" *");
//		printf("\n");	  
//	}

//		int i, j,k,n = 5;
//	for(i=1;i <= n; i++)
//	{
//		for(j = 1; j <= n-i; j++)
//			  printf(" ");
//	  	for(k = 1; k <= i; k++)
//			    printf(" *");
//		printf("\n");	  
//	}
//		int i, j,k,n = 5;
//	for(i=1;i <= n; i++)
//	{
//		for(j = 1; j <= i; j++)
//			  printf(" ");
//	  	for(k = n; k >= i; k--)
//			    printf("*");
//		printf("\n");	  
//	}
	
//			int i, j,k,n = 5;
//	for(i=1;i <= n; i++)
//	{
//		for(j = 1; j <= i; j++)
//			  printf(" ");
//	  	for(k = n; k >= i; k--)
//			    printf(" *");
//		printf("\n");	  
//	}

//    int i, j,k,n = 5;
//	for(i=n;i >=1; i--)
//	{   
//	   for(k = 0; k <= n-i; k++)
//			    printf("*");
//		for(j = 0; j < 2*i-2; j++)
//			  printf(" ");
//	  	for(k = 0; k <= n-i; k++)
//			    printf("*");
//		printf("\n");	  
//	}
//	int i, j,k,n = 5;
//	for(i=n;i >=n; i--)
//	{   
//	   for(k = 1; k <= i; k++)
//			    printf("*");
//		for(j = n; j >=2*(n-i); j--)
//			  printf(" ");
//	  	for(k = 1; k <= i; k++)
//			    printf("*");
//		printf("\n");	  
//	}
  
  
//  int i, j,k,n = 3;
//	for(i=n;i >=1; i--)
//	{
//		for(j = 1; j <= i-1; j++)
//			  printf(" ");
//	  	for(k = n; k >= i; k--)
//			    printf("*");
//		printf("\n");	  
//	}
//	for(i=n-1;i >=1; i--)
//	{
//	
//	for(j = n-1; j>=i; j--)
//			  printf(" ");
//	  	for(k = 1; k <= i; k++)
//			    printf("*");
//    printf("\n");
//			}

//
//int i, j,n = 5;
//	for(i=0;i <= n; i++)
//	{
//		for(j = 0; j < i; j++)
//			  printf("%d",i);
//		printf("\n");	  
//	}
	
/*
1
22
333
4444
55555
*/


int i, j,n = 26;
	for(i=1;i <= n; i++)
	{
		for(j = 1; j <= i; j++)
			  printf(" %c",j+64);
		printf("\n");	  
	}
	
}
