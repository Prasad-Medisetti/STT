#include <stdio.h>
int main()
{
	char a[20],b[20];
	scanf("%s",a);
	scanf("%s",b);
	int c = StrCmp(a,b);
	if(c<0)
		printf("%s %s",b,a);
	else if(c>0)
		printf("%s %s",a,b);
	else
		printf("Same");
	return 0;
}
int StrCmp(char* p,char* q)
{
	for(;*p==*q;p++,q++);
	return *p-*q;	
}
