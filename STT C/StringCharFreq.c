/*
3.	Take a string contains only alphabets. Now your task is to print each character followed by its frequency in alphabetical order.
	Input:
		aditya
	Output:
		a2d1i1t1y1
*/
#include <stdio.h>
int main()
{
	char str[100],freq[25] = {0},f[25]={0};
	int i,n;
	printf("Enter a string containing only alphabets:\n");
	scanf("%s",&str);
	for(i=0;str[i] != '\0';i++)
	{
		if(str[i] >= 65 && str[i] <= 90)
			freq[str[i] - 65]++;
		if(str[i >= 97 && str[i] <= 122])
	 		freq[str[i] - 97]++;
	}
	for(i=0;str[i] != '\0';i++)
	{
		if(str[i] >= 65 && str[i] <= 90 && freq[str[i]-65] >=1)
		{
			printf("%c%d",str[i],freq[str[i] - 65]);
			freq[str[i]-65]=0;
		}
		if(str[i >= 97 && str[i] <= 122] && freq[str[i]-97] >=1)
		{
			printf("%c%d",str[i],freq[str[i] - 97]);
			freq[str[i]-97]=0;
		}
	}
	return 0;
}
