#include <stdio.h>
void Reverse(char[],int);
int StrLen(char[]);
int main()
{
	char s[50];	
	printf("Enter a String:\n");
	scanf("%[a-zA-z0-9 ]",s);
	printf("Reverse of \"%s\" is :\n\"",s);
	Reverse(s,StrLen(s));
	printf("\"");
	return 0;
}
int StrLen(char s[])
{
	int i=0;
	while(s[i]!='\0')
		i++;
	return i;
}
void Reverse(char s[],int n)
{
	if(n>0)
	{
		printf("%c",s[--n]);
		Reverse(s,n);
	}
	return;
}
