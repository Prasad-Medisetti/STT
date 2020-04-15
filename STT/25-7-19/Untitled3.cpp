#include<stdio.h>
int strc(char *,char *);
int main()
{
	char a[5],b[5];
	int c;
	scanf("%s",a);
	scanf("%s",b);
	c=strc(a,b);
	if(c<0)
	printf("b,a");
	else if(c>0)
	printf("a,b");
	else
	printf("same");
	return 0;
}
    int strc(char *p,char *q)
{
	for(;*p==*q;p++,q++)
	return *p-*q;
}
