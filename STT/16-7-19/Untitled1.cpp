#include<stdio.h>
int main()
{
	int i=0;
	char str1[20],str2[20];
	printf("Enter strings");
	scanf("%s %s",str1,str2);
	while(i!='\0')
	{
		if(str2[i]==str1[i])
		i++;
		else
		{
			printf("Not equal");
			return 0;
		}
	}printf("Equal strings");
	return 0;
}
