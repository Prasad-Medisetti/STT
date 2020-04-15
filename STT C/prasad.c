#include <stdio.h>
#include <string.h>
int main()
{
	char s[10];
	int n,i,j=0,k=0;
	printf("Enter a String:\n");
	scanf("%[a-zA-Z]",s);
	n = strlen(s);
	for(i=0;i<n;i++)
	{
		if(j<n)
		{
			printf("%c\n",s[j++]);
		 	continue;
		}
		for(k=i;k<=n-i;k++)
		{
			printf("%c",s[k]);
		}
	}
	return 0;
}
