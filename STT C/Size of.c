#include <stdio.h>
int main()
{
	int a = 5,*b;
	float f = 3.14,*g;
	char c = 'a',*h;
	double d = 2.3,*e;
	signed int s,*p;
	printf("int\tsigned int\t\tfloat\tchar\tdouble\n");
	printf("%d\t%d\t\t\t%d\t%d\t%d\n",&a,&s,&f,&c,&d);
	printf("%d\t%d\t\t\t%d\t%d\t%d\n",sizeof(a),sizeof(s),sizeof(f),sizeof(c),sizeof(d));	
	printf("%d\t%d\t\t\t%d\t%d\t%d",sizeof(p),sizeof(p),sizeof(g),sizeof(h),sizeof(e));	
	return 0;
}
