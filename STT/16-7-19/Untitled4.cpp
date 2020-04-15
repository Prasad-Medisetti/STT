#include<stdio.h>
#include<string.h>
int main()
{
	int i=0,n;
	char str[20];
	printf("Enter string");
	scanf("%s",str);
	n=strlen(str);
	for(i=0;i<=n;i++)
	{
	
	if(str[i]!=str[n-i-1])
	{
		printf("No");
		return 0;
	}
	}
	printf("Yes");
	return 0;
}
