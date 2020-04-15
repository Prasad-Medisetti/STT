#include <stdio.h>
#include <string.h>
 
void main()
{
    char s[200];
    int words = 0, letters=0,lines=0,i;
	
    printf("enter the string\n");
    scanf("%[^\n]s", s);
    for (i = 0;s[i] != '\0';i++)
    {
        if (s[i] == ' ')
            words++;    
        if (s[i]== '\n')
        	lines++;
    }
    printf("number of words in given string are: %d\n", words + 1);
    printf("number of lines in given string are: %d\n", lines + 1);
   // printf("number of letters in given string are: %d\n", letters + 1);
}
