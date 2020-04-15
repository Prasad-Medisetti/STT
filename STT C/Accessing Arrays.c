#include <stdio.h>
int main()
{
	int a[3][2] = {0}, i, j, *p;
	for(i=0;i<3;i++)
	{
		p = a[i];
		for(j=0;j<2;j++)		
			printf("%u ", *(p+j));
//			printf("%u ", (*(a+i)+j));
//		for(j=0;j<2;j++)
//			printf("%d ", p[i]);
		printf("\n");
	}
	return 0;
}
