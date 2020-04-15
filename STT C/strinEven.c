#include<stdio.h>
#include<stdlib.h>
int main()
{
	char str[10];
	int even[10],j,k;
	printf("Enter digits:");
	for(j=0;j<10;j++)
	scanf("%c", &str[j]);
	for(j=0;j<10;j++)
	{ 
 	    k=0;
	    j=atoi(str[j]);
	    printf("%d ",j);
//		if(j%2==0)
//		{
//		 even[k]=j;	
//		 k++;
//		}	
		 
	}
	for(j=0;j<k;j++)
	  printf("%d ",even[j]);
	  return 0;
}
