#include <stdio.h>
int main()
{
//	int a = 5;
//	int *x = &a;
//	int **y = &x;
//	printf("a\t*x\t**y\n");
//	printf("%d\t%d\t%d",a,*x,**y);
	int a = 5;
	int *x = &a;
	printf("%p --> %d\n",x,*x);
	(*x)++;
	printf("%p --> %d\n",x,*x);
//	int a[5] = {1, 2, 3, 4, 5},i;
//	int (*x)[5];
//	x = &a;
//	printf("%p\n%p",x,a);
//	for(i=0;i<10;i++)
//		printf("\n%d",x[i]);
	return 0;
}
