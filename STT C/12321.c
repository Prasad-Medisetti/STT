#include <stdio.h>
void main()
{
	//right space
//	int n = 5, i, j,k;
//	for(i = 1; i <= 2*n-1; i++)
//	{
//		j = i<=n?i:n-(i%n);
//		for(k=1;k<=j;k++)
//			printf("*");
//		printf("\n");
//	}

//left spaces
//	int n = 5, i, j,k,l;
//	for(i = 2*n-1; i >= 1; i--)
//	{
//		j = i<=n?i:n-(i%n);
//		for(l=1;l<=n-j;l++)
//			printf(" ");
//		for(k=1;k<=j;k++)
//			printf("*");
//		printf("\n");
//	}
//	int n = 5, i, j,k,l;
//	for(i = 2*n-1; i >= 1; i--)
//	{
//		j = i<=n?i:n-(i%n);
//		for(l=1;l<=n-j;l++)
//			printf(" ");
//		for(k=1;k<=2*j-1;k++)
//			printf("*");
//		printf("\n");
//	}

//
//	int n = 5, i, j,k,l;
//	for(i = 1; i <=n; i++)
//	{
//		j = i<=n?i:n-(i%n);
//		for(l=1;l<=n-j;l++)
//			printf(" ");
//		for(k=1;k<=2*j-1;k++)
//			printf("*");
//		printf("\n");
//	}
	/*
	    *
	   ***
	  *****
	 *******
	*********
	*/
	
//		int n = 5, i, j,k,l;
//	for(i = 1; i <=2*n-1; i++)
//	{
//		j = i<=n?i:n-(i%n);
//		j=n-j+1;
//		for(k=1;k<=2*j-1;k++)
//			printf("*");
//		printf("\n");
//	}
/*
*********
*******
*****
***
*
***
*****
*******
*********
*/

	int n = 5, i, j,k,l;
	char ch[]={'A','D','I','T','Y','A'};
	for(i = 1; i <=2*n-1; i++)
	{
		j = i<=n?i:n-(i%n);
		j=n-j;
		for(k=0;k<=2*j-1;k++)
			printf("%c",ch[k-1]);
		printf("\n");
	}
	
	
}
