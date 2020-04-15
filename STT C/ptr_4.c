#include <stdio.h>
int main()
{
//	int a[10] = {1,2,3}, *p;
//	printf("%u, %u, %u, %u", a, &a[0], a+1, &a[0]+1);
//	p = a;
//	printf("%u, %u", p, ++p);
//	char a[20] = "aditya", b[10] = "adisri";
//	char *p = a, *q = b;
//	for(;*p != '\0';p++);
//	for(;*q != '\0';q++)
//	{
//		*p = *q;
//		p++;
//	}
//	*p = '\0';
//	printf("%s\n",a);
//	compare two strings
	char a[20] = "prasad", b[10] = "d.v.sai";
	char *p = a, *q = b;
	for(;*p == *q;p++,q++);
//	{
//			if(*p == *q)
//				continue;
//		 	else
//		 		break;
//	}
	if(*p < *q)
				printf("%s\t%s",a,b);
	if(*p > *q)
				printf("%s\t%s",b,a);
	return 0;
}
