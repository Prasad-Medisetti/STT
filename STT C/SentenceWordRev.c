/*
3.	Write a C program which reads a line full of text into a character array and replace all the words in 
	reverse order within it and then display the array.
	Sample input: 	This is Coding Platform 
	Sample output: 	sihT si gnidoC mroftalP
*/
#include <stdio.h>
int main()
{
	char str[100],*s,*r;
	int len;
	printf("Enter a Sentence:\n");
	gets(str);
	for(s=str;*s;s++)
	{
		for(;*s!=' '&&*s!='\0';s++);
		if(*s==' '||*s=='\0')
		{
			for(r=s-1;*r!=' '&&r>=str;r--)
				printf("%c",*r);
			if(*s==' ')
				printf("%c",*r);
			if(*s=='\0')
				break;
		}
	}
	return 0;
}
