#include <stdio.h>
#include <math.h>
int main()
{
	int num,n,a,b,c,count;
	printf("Enter a 4 digit no: \n");
	scanf("%d",&num);
	n = num;
	c = log10(n);
//	printf("%d",c);
	while(c >= 0)
	{
		a = n % 10;
		n = n / 10;
		b = n % 10;
		if(a == b || a == b+1)
			count++;
		c--;
	} 
	if(count == 4)
		printf("%d is a Fancy Number",num);
	else
		printf("%d is not a Fancy Number",num);
		return 0;
}
