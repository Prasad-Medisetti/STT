/*
4.	Take a string contains alphabets, symbols and digits. Now your task is to remove characters in the given string except alphabets.
	Sample Input: 
		   pr'og2^ram-ming 
	Output: 
			programming
*/
#include <stdio.h>
int main()
{
	char str[100];
	int i,j,n;
	printf("Enter a string containing only alphabets:\n");
	scanf("%s",&str);
	for(i=0;str[i] != '\0';i++)
	{
		if((str[i] >= 65 && str[i] <= 90) || (str[i] >= 97 && str[i] <= 122))
			continue;
	 	for(j=i;str[j] != '\0';j++)
			str[j] = str[j+1];
		i=-1;
	}
	printf("%s",str);
	return 0;
}
