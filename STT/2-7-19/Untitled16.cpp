#include<stdio.h>
#include<math.h>
int main()
{
	int a,n;
	printf("ENTER NUMBER");
	scanf("%d",n);
	a=round(sqrt(n));
	printf("%d",a*a);
	return 0;
}
