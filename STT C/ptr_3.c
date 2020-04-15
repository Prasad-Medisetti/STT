#include <stdio.h>
int main()
{
 	int a[5] = {10, 20, 30, 40, 50}, *p, i, sum = 0;
	p = a;
//	printf("%p --> %p\n",a, p);
//	for(i = 0;i < 5;i++)
//		printf("%p\t",&a[i]);
//	printf("\n");
//	for(i = 0;i < 5;i++)
//	printf("%d\t",*p++);
//		printf("\n");
	for(i = 0;i < 5;i++)
		printf("%d ",*(p+i));
	for(i = 0;i < 5;i++)
		sum += *(i+p);
    printf("\nSum : %d", sum);
    printf("\n");
    return 0;
}
