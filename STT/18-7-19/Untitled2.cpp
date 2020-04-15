#include<stdio.h>
int main()
{
	int a=5,*p;
	float b=3.251666,*q;
	char c='b',*r;
	double d=2.555,*s;
	p=&a;q=&b;r=&c;s=&d;
	printf("%d - %d - %d - %d",sizeof(p),sizeof(q),sizeof(r),sizeof(s));
//	printf("%p - %p - %p - %p",p,q,r,s);
	return 0;
}
