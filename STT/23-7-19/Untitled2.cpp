#include<stdio.h>
int main()
{
	char a[20]="aditya",b[10]="sri";
	char *p=a,*q=b;
	for(;p!='\0';p++);
	for(;q!='\0';q++)
	{
		*p=*q;
		p++;
	}
	*p='\0';
	printf("%s\n",a);
	return 0;
}
