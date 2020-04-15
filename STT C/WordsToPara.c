#include <stdio.h>
int main()
{
	int i=0, j=0, noOfLines=0, noOfWords = 0, lineBreak[100]={0};
	char para[1000], words[100][100], para2[1000];
	scanf("%[a-zA-Z \n]",para);
	for(i=0;para[i] != '\0';i++)
	{
		if(para[i] == ' ' || para[i] == '\n')
		{
			if(para[i] == '\n')
			{
				lineBreak[noOfLines++] = noOfWords;
			}			
			words[noOfWords][j] = '\0';
			noOfWords++;
			j=0;
			continue;
		}
		words[noOfWords][j++] = para[i];
	}
	int k=0;
	noOfLines = 0;
	for(i=0;i<=noOfWords;i++)
	{
		for(j=0;words[i][j] != '\0';j++)
		{
			para2[k++] = words[i][j];
		}
		if(words[i][j] == '\0' && lineBreak[noOfLines] == i)
		{
			para2[k++] = '\n';
			continue;
		}
		para2[k++] = ' ';
	}
	para2[k]='\0';
	system("cls");
	printf("Actual Paragraph:\n");
		printf("%s",para2);
	printf("\n\nSeperated Words:\n");
	for(i=0;i<=noOfWords;i++)
		printf("%s\n",words[i]);
	printf("\n\nCombined Words to paragraph:\n");
		printf("%s",para2);
	return 0;
}
