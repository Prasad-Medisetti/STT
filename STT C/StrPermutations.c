//	String Permutations
#include <stdio.h>
int main()
{
	char str[20];
	int i,j,k,len;
	printf("Enter a String:\n");
	gets(str);
	printf("Given String Permutations:\n");
	for(len=0;len[str]!='\0';len++);
	for(i=0;i<len;i++)
	{
		for(j=0;j<len;j++)
		{
			for(k=0;k<len;k++)
			{
				printf("%c%c%c\n",str[i],str[j],str[k]);
			}
		}
	}
	return 0;
}
