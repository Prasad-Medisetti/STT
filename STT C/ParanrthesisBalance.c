#include <stdio.h>
int main()
{
	char str[20],*c;
	int cnt=0,Nested=0;
	printf("Enter a String only containing paranthesis:\n");
	gets(str);
	for(c=str;*c!='\0';c++)
	{
		if(*c=='(')
		{
			cnt++;
			if(*(c+1)=='(')
				Nested++;
		}
		else if(*c==')')
			 cnt--;
		else
			continue;	 
	}
	if(cnt==0)
		printf("\nBalanced, Nesting Level=%d",Nested);
	else
		printf("\nUnbalanced, Nesting Level=%d",Nested);
	return 0;
}
