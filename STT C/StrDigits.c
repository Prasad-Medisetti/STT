#include <stdio.h>
int main()
{
	char str[10];
	int i;
	printf("Enter Elements: ");
	for(i=0;i<10;i++)
	{
		scanf("%c",&str[i]);
	}
	for(i=0;i<10;i++)
 		printf("%c",str[i]);
	return 0;
}
