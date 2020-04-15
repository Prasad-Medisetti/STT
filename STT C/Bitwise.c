#include<stdio.h>
void bin(short int n)
{
	int i;
		  printf("\n%d\t",n);
	for(i = 15;i >= 0;i--)
	{
	
		  n & (1 << i) ? printf("1") : printf("0");
		 if(i==8) printf(" ");
	
	}

	  return;	
}
void main()
{
	 short int a =2,b=4;
	  bin(a);
	  bin(b);
	  bin(a&b);
	  bin(a|b);
	  bin(a^b);
	  bin(~a);
      bin(~b);
 }
