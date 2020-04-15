#include <stdio.h>
int main()
{
	char para[100];
	int i,j,s;
	printf("Enter Shift Value: \n");
	scanf("%d",&s);
	printf("Enter a paragraph with spaces, new lines: \n");
	scanf("%[A-za-z \n]",para);
	system("cls");
	printf("Entered paragraph is:\n%s\n",para);
	for(i = 0;para[i] != '\0';i++)
//		printf("%c",para[i]);
	{
		if(para[i] == ' ')
			printf(" ");
		else if(para[i]+s <= 122)
	 		para[i] = para[i]+s;
		else
			para[i] = para[i-26]+s;
	}
	printf("Paragraph shifted by %d is:\n%s\n",s,para);
	
	return 0;
}
