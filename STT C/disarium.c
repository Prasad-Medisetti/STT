#include <stdio.h>
#include <math.h>
int main()
{
	int num, n, i, sum = 0;
	printf("Enter a number: \t");
	scanf("%d", &num);
	n = num;
	for(i = log10(n)+1;n > 0;i--)
	{
		sum += pow(n % 10, i);
		n = n / 10;
	}
	if(num == sum)
		printf("%d is a disarium number.", num);
	else
		printf("%d is not a disarium number.", num);
	return 0;	
}
