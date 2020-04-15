#include<stdio.h>
int main()
{
	char a[20]="aditya",b[10]="adisri";
	char *p=a,*q=b;
	for(;p!='\0';p++);
	for(;q!='\0';q++)
	{
		if(*p==*q)
		p++;
		else
		{
		printf("Failed");
		return 0;
	}
	}
	*p='\0';
	printf("%s\n",a);
	return 0;
}
