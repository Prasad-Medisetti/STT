#include <stdio.h>
int main()
{
	int i=0, j=0, noOfWords = 0;
	char para[1000], words[100][100];
	scanf("%[a-zA-Z \n]",para);
	for(i=0;para[i] != '\0';i++)
	{
		if(para[i] == ' ' || para[i] == '\n')
		{
			words[noOfWords][j] = '\0';
			noOfWords++;
			j=0;
			continue;
		}
		words[noOfWords][j++] = para[i];
	}
	system("cls");
	printf("%s",para);
	printf("\n\nSeperated Words:\n");
	for(i=0;i<=noOfWords;i++)
		printf("%s\n",words[i]);
	return 0;
}
