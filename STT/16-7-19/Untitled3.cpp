#include<stdio.h>
int main()
{
	int i=0;
	char str[20];
	printf("Enter string");
	scanf("%s",str);
	while(str[i]!='\0')
	{
	
	if(str[i]>=48&&str[i]<=57)
		i++;
	else
	{
		printf("No");
		return 0;
	}
	}
	printf("Yes");
	return 0;
}
