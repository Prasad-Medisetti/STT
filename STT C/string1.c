#include<stdio.h>
int main()
{
	int n=10,i;
	char str[n];
	printf("Enter the string: ");
	scanf("%[a-z]",&str);
    for(i=0;i<n;i++)
       printf("%c",str[i]);
      
}
