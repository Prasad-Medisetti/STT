//program to check whether the given string contains all the alphabets from a-z
#include<stdio.h>
int main()
{
	char a[100]={0},str[100],i,j,k=97;
	printf("Enter the String:");
	scanf("%[a-z]",&str);
	for(i=0;str[i]!='\0';i++)
	{
		a[str[i]-97]++;//counter for the characters present in the entered string
	}
	for(i=0;i<26;i++)
	{
		if(a[i]==0)
		  break;
	}
	if(i<26)
	  printf("Given string does not contains all the characters from a-z");
	else
	printf("Given string contains all the characters from a-z");
	return 0;
}
