#include <stdio.h>
int main()
{
	int i=0, n = 0,flag = 0;
	char str[20],s[20];
	printf("Enter a String: \n");
   	scanf("%s", str);
   	n = strlen(str);
   	for(i=0;i < n/2;i++)
   	{
	   if(str[i] != str[n-i-1])
	   {
   	   		flag++;
   	   		break;
	   }
	}
 	if(flag)
		printf("%s is a palindrome and Reversed string is %s",str,s);
	else
		printf("%s is not a palindrome.",str);
	return 0;
}
