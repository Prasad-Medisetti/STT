#include<stdio.h>
void bin(short int n,int s)
{
	int i;
	for(i = 15;i >= 0;i--)
	{
	
		  n & (1 << i) ? printf("1") : printf("0");
		 if(i==8) printf(" ");
	
	}
	  printf("\t%d\n",s);
	  return;	
}
void main()
{
	 short int a = -32768,i;
	for(i = 0;i<=16;i++)
	{
		  printf("%d\t",a>>i);
			 bin(a>>i,i);
 }
//	printf("\n");
//	bin(a<<2);
}
