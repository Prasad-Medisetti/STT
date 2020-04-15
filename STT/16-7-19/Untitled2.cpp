#include<stdio.h>
int main()
{
	int i=0;
	char str[20];
	printf("Enter string");
	scanf("%s",str);
	if(str[i]<str[i+1])
		i++;
	else
	{
		printf("Not in a strict order");
		return 0;
	}
	printf("Strict ordered string");
	return 0;
}
