#include <stdio.h>
int main()
{
	char para[100];
	int i,w=0,l=1,s=0,c=0;
	printf("Enter a paragraph with spaces, new lines: \n");
	scanf("%[A-za-z \n]",para);
	for(i = 0;para[i] != '\0';i++)
//		printf("%c",para[i]);
	{
		if(para[i] == ' ')
			s++;
		if(para[i] == ' ' && para[i+1] != ' ')
			w++;
		if(para[i] == '\n')
			l++;
		c++;	
	}
	printf("\nNo.of spaces : %d",s);
	printf("\nNo.of characters : %d",c);
	printf("\nNo.of words : %d",w+l);
	printf("\nNo.of Lines : %d",l);	
	return 0;
}
