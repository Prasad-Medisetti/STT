#include <stdio.h>
#include <string.h>
int SubStrings(char*,int);
int main()
{
	char s[50];
	int n,count;
	printf("Enter a String:\n");
	scanf("%[a-zA-Z]",s);
	n = strlen(s);
	count = SubStrings(s,n);
	printf("\nNumber of SubStrings possible for \"%s\" are : %d",s,count);
	return 0;
}
int SubStrings(char *s,int n)
{
	int i,j,k,l,c=0;
	printf("SubStrings are :\n");
	for(i=0;i<n;i++)
	{
		for(j=0;j<n-i;j++)
		{
			k=i+j;
			for(l=j;l<=k;l++)
				printf("%c ",s[l]);
			printf("\n");
			c++;		 	
		}
	}
	return c;
}
