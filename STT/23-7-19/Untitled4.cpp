#include<stdio.h>
int main()
{
	char a[20]="aditya",b[10]="adisri";
	char *p=a,*q=b;
	int diff;
	for(;*p==*q;p++,q++);
	diff=*p-*q;
	if(diff>0)
	printf("%s %s \n",a,b);
	else if(diff<0)
	printf("%s %s \n",b,a);
	else
	printf("Both are same");
	return 0;
}
