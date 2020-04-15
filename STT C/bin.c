#include<stdio.h>
void bin(int n)
{
	int i;
	for(i = 31;i >= 0;i--)
		  n & (1 << i) ? printf("1") : printf("0");
		  return;
}
void main()
{
	int a = 10;
	bin(a);
}
